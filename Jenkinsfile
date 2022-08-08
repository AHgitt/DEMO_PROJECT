pipeline {
    agent { label 'new_node' }
    stages {
        stage('build') {
            steps {
                script {
					bat 'docker stop flask_app'
					bat 'docker stop flask_phpmyadmin'
					bat 'docker stop flask_mysql'
					bat 'docker rm flask_app'
					bat 'docker rm flask_phpmyadmin'
					bat 'docker rm flask_mysql'
                    bat 'docker-compose up -d --build'
                }
            }
        }
    }
}
