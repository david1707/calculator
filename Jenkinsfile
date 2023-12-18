pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
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