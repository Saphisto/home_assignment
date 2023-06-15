pipeline {
    agent {
        label 'zip-job-docker'
    }
    // environment {
    //     ARTIFACTORY_URL = 'https://artifactory-xx'
    //     ARTIFACTORY_USER = 'superman'
    //     ARTIFACTORY_PASSWORD = 'P@ssw0rd123$'
    //     VERSION = env.VERSION // Make sure to set the VERSION environment variable
    // }
    stages {
        stage('Checkout SCM') {
            steps {
                deleteDir()
                git branch: 'main', url: 'git@github.com:Saphisto/home_assignment.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 /tmp/zip_job.py'
            }
        }
        // stage('Publish') {
        //     when {
        //         expression { currentBuild.result == 'SUCCESS' }
        //     }
        //     steps {
        //         script {
        //             def zipFiles = findFiles(glob: '**/*.zip')
        //             zipFiles.each { zipFile ->
        //                 def targetPath = "store-artifacts/${VERSION}/${zipFile.getName()}"
        //                 rtUpload serverId: 'artifactory-xx', spec: """{
        //                     "files": [
        //                         {
        //                             "pattern": "${zipFile.path}",
        //                             "target": "${targetPath}"
        //                         }
        //                     ]
        //                 }"""
        //             }
        //         }
        //     }
        // }
        stage('Report') {
            steps {
                emailext recipientProviders: [requestor()],
                subject: "Job Status: ${currentBuild.currentResult}",
                body: "The job status is ${currentBuild.currentResult}."
            }
        }
    }
    post {
        always {
            deleteDir()
        }
    }
}
