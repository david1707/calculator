pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                git url: 'https://github.com/david1707/calculator', branch: "main"
                sh "python3 --version"
            }
        }
        stage("Testing") {
            steps {
                sh "python3 -m unittest test_calculator"
            }
        }
    }
}