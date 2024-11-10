pipeline {
    options { timestamps() }

    agent none
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
        stage('Create Docker Image') {
            agent any
            steps {
                script {
                    def imageName = "sergoo/lab4-jenkins:${BUILD_NUMBER}"
                    sh "docker build -t ${imageName} ."
                    env.IMAGE_NAME = imageName
                }
            }
        }
        stage('Upload to Docker Hub') {
            agent any
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                    sh "docker push ${env.IMAGE_NAME}"
                }
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3.12'
                    args '-u root'
                }
            }
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install --no-cache-dir virtualenv'
                sh 'virtualenv venv'
                sh 'venv/bin/pip install --no-cache-dir pytest pytest-cov'
                sh 'venv/bin/python app_test.py'
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