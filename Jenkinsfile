pipeline {
    options { timestamps() }
    agent none
    environment {
        DOCKER_CREDI = credentials('docker') // Ім'я "docker" має співпадати з існуючим налаштуванням
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
        stage('Docker Login') {
            agent any
            steps {
                script {
                    // Замість значень 'your-username' та 'your-password' використовуйте секрети Jenkins або змінні середовища
                    sh 'echo $DOCKER_CREDI_PSW | docker login --username $DOCKER_CREDI_USR --password-stdin'

                }
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
            stage('Docker Login') {
            agent any
            steps {
                script {
                    // Замість значень 'your-username' та 'your-password' використовуйте секрети Jenkins або змінні середовища
                    sh 'echo $DOCKER_CREDI_PSW | docker login --username $DOCKER_CREDI_USR --password-stdin'
                }
            }
        }
        }
    }
}
