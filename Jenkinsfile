pipeline {
    agent {
        docker {
            image 'shay/home_assignment:version1'
            label 'zip-job-docker'
            args '--privileged'
        }
    }
    stages {
        stage('Checkout SCM'){
            steps {
                sh 'rm -rf *'
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs : [[
                        url: 'git@github.com:Saphisto/home_assignment.git',
                        credentialsId: ''
                    ]]
                ])
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.image('ubuntu:latest').inside {
                        sh 'python3 /tmp/zip_job.py'
                    }
                }
            }
        }
    }
}
