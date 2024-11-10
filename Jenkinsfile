pipeline {
    options {
        timestamps()
    }
    agent none
    stages {
        stage('Check SCM') {
            agent any
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Building ${BUILD_NUMBER}"
                echo "Build complete"
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'alpine'
                    args '-u "root"'
                }
            }
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install xmlrunner'
                sh 'python test_notebook.py'
            }
            post {
                always {
                    junit "test-reports/*.xml"
                }
                success {
                    echo "Success"
                }
                failure {
                    echo "Failure"
                }
            }
        }
    }
}
