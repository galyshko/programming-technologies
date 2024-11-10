pipeline {
    options { timestamps() }

    agent any
    triggers {
        cron('H 0 * * *')
        pollSCM('H 20 * * * ')
    }
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Building...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }

        stage('Test') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install --no-cache-dir pytest pytest-cov'
                sh 'pytest test_notebook.py'
            }
            post {
                always {
                    echo "Test stage completed"
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }
        }
    }
}
