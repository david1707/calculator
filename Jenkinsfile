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
                sh "coverage run -m unittest test_calculator"
                sh "coverage report"
                //sh "python3 -m unittest test_calculator"
            }
        }
    }
}