pipeline {
    agent { label 'new_node' }
    stages {
        stage('build') {
            steps {
                script {
                    bat 'docker-compose up -d --build'
                }
            }
        }
    }
}
