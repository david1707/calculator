pipeline {
    agent any
    stages {
        stage('Checkout repo') {
           steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHub-Tokens', url: 'https://github.com/david1707/calculator.git']])
                sh "python3 -V"
           }
        }
        stage('Downloading repo') {
           steps {
                git branch: 'main', url: 'https://github.com/david1707/calculator.git'
           }
        }
        stage('Testing') {
           steps {
                sh 'python3 -m pytest'
           }
        }
    }
}
