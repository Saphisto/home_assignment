pipeline {
    agent {
            label 'zip-job-docker'
            args '--privileged'
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
