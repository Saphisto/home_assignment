pipeline {
    agent {
        docker { image 'shay/home_assignment:version1' }
    }
    stages {
        stage('Checkout SCM'){
            steps {
                sh 'rm -rf *'
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs : [[
                        url: 'git@github.com:Saphisto/project_traininf.git',
                        credentialsId: ''
                    ]]
                ])
            }
        }
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}
