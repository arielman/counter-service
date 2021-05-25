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
                    sh 'docker build . -t arielma2304/my-repo:latest'
                }
            }
        }
}
