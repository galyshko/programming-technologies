pipeline {
    options { timestamps() }
    agent none
    environment {
        DOCKER_TLS_CERTDIR = ''
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
                echo "Building ${BUILD_NUMBER}"
                echo "Build complete"
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'alpine'
                    args '--rm -u="root"'
                }
            }
            steps {
                sh 'apk update && apk add python3 py3-pip'
                sh 'pip install --upgrade pip'
                sh 'pip install xmlrunner'
                sh 'python3 test_notebook.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
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
