pipeline {
    agent {
        label 'zip-job-docker'
    }
    environment {
        DOCKER_OPTS = '-u root'
        ARTIFACTORY_USER = 'superman'
        ARTIFACTORY_PASSWORD = 'P@ssw0rd123$'
    }
    stages {
        stage('Checkout SCM') {
            steps {
                deleteDir()
                git branch: 'main', credentialsId: 'for_git_hib_ssh', url: 'git@github.com:Saphisto/home_assignment.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 /tmp/zip_job.py'
            }
        }
        stage('Publish') {
            steps {
                script {
                    sh '''
                    # Directory path where the files are located
                    directory="/home/ubuntu/workspace/home_assignment/"
                    # Artifactory URL
                    artifactory_url="http://192.168.126.128:8082/artifactory/store-artifacts/"
                    # Username and password for authentication
                    username="superman"
                    password="P@ssw0rd123$"
                    # Iterate over files in the directory
                    for file in "$directory"/*; do
                      # Check if the current item is a file
                      if [[ -f "$file" ]]; then
                        # Extract the file name from the path
                        filename=$(basename "$file")
                        # Upload the file to Artifactory using curl
                        curl -u "$username":"$password" -X PUT "$artifactory_url/$filename" -T "$file"
                        # Check the response code if needed
                        # response=$(curl -u "$username":"$password" -X PUT "$artifactory_url/$filename" -T "$file" -w "%{http_code}" -o /dev/null)
                        # echo "Response code: $response"
                      fi
                    done

                    
                    '''
                    
                }
            }
        }
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
