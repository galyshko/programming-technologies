pipeline {
    options { timestamps() }
    agent none
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker') // Ім'я "docker" має співпадати з існуючим налаштуванням
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
                echo "Building ... ${BUILD_NUMBER}"
                echo "Build completed"
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'alpine'
                    args '-u="root"'
                }
            }
            steps {
                sh 'apk add --update python3 py3-pip'
                sh 'python3 -m venv /venv'
                sh 'source /venv/bin/activate && pip install unittest-xml-reporting'
                sh 'source /venv/bin/activate && python3 test_notebook.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Testing successful"
                }
                failure {
                    echo "Tests failed"
                }
            }
        }
        stage('Login to Docker Hub') {
    steps{
	sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
	echo 'Login Completed'
    }
}
stage('Push Image to Docker Hub') {
    steps{
 sh 'sudo docker push sergoo/lab4-jenkins:$BUILD_NUMBER'
echo 'Push Image Completed'
    }
}
    }
}
