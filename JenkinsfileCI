pipeline {
    agent {label 'linux'}
        stages {
            stage('Checkout external proj') {
                steps {
                    git branch: 'dev',
                        credentialsId: 'arielman',
                        url: 'https://github.com/arielman/counter-service.git'
                    sh "ls -lat"
                }
            }
            stage('Docker build') {
                steps {
                    sh 'sudo docker build . -t arielma2304/my-repo:$(date +"%d%m%y")'
                    sh 'sudo docker tag arielma2304/my-repo:$(date +"%d%m%y") arielma2304/my-repo:latest'
                }
            }
            stage('Push image to DockerHub') {
                steps {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'dockerhub_pass', usernameVariable: 'dockerhub_user')]) {
                        sh 'sudo docker login --username ${dockerhub_user} --password ${dockerhub_pass}'
                        sh 'sudo docker push arielma2304/my-repo:$(date +"%d%m%y")'
                        sh 'sudo docker push arielma2304/my-repo:latest'
                    }    
                }
            }
        }
}
