pipeline {
    agent {
        docker {
            label 'zip-job-docker'
            args '--privileged'
            reuseNode true
    }
    stages {
        stage('Checkout SCM') {
            steps {
                deleteDir() // Instead of 'rm -rf *', use deleteDir() to clean workspace
                git branch: 'main', url: 'git@github.com:Saphisto/home_assignment.git'
            }
        }
    }
}
