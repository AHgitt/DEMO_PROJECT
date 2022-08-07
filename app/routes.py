from flask import render_template, flash, redirect, url_for, request
from app import flask_app, db
from app.models import Sites, Rows
from app.forms import CreateForm, UpdateForm
import http.client as httplib


@flask_app.route('/index')
@flask_app.route('/')
def index():

    sites = Sites.query.all()
    rows = Rows.query.all()
    status = []
    for x in sites:
        try:
            c = httplib.HTTPConnection(x.site_url)
            c.request("HEAD", '')
            if c.getresponse().status < 400:
                status.append(True)
                print("YES")
            else:
                status.append(False)
                print("NO")
        except:
            status.append(False)
            print("Website does not exist")

    #Python can't iterate over the same zip twice
    data1 = zip(sites, status)
    data2 = zip(sites, status)
    data3 = zip(sites, status)

    return render_template('index.html', title='Home', data1=data1, data2=data2, data3=data3, fonts=rows)

#Modify Website
@flask_app.route('/modifysite/<url>', methods=['GET', 'POST'])
def modify_site(url):

    site = Sites.query.filter_by(site_url=url).first()
    form = UpdateForm(row=int(site.row_id)-1)

    #Populate the text boxes with values from database
    if request.method == 'GET':
        form.url.data = site.site_url
        form.colour.data = site.site_colour
        return render_template('modifysite.html', form=form)

    if form.validate_on_submit():
        if form.submit.data:

            site.site_url = form.url.data
            site.site_colour = form.colour.data
            site.row_id = form.row.data
            db.session.commit()
            flash("Website values have been changed")
            return redirect(url_for('modify_site', url=form.url.data))
        elif form.submit2.data:

            db.session.delete(site)
            db.session.commit()
            flash("Website has been removed")
            return redirect(url_for('index'))
    return render_template('modifysite.html', title='Modify Site', form=form, url=url)

#Add Website
@flask_app.route('/addsite', methods=['GET', 'POST'])
def add_site():
    form = CreateForm()
    if form.validate_on_submit():
        site = Sites(site_url=form.url.data, site_colour=form.colour.data, row_id=form.row.data)
        db.session.add(site)
        db.session.commit()
        flash("Site has been added to the list")
        return redirect(url_for('add_site'))
    return render_template('addsite.html', title='Adding a Website', form=form)
