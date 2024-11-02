pipeline {
    options { timestamps() }
    agent none
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        } 
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        } 
        stage('Test') {
            agent { 
                docker { 
                    image 'python:3.12-alpine' 
                    args '-u="root"'
                } 
            }
            steps {
                sh 'apk add --no-cache py3-pip'
                sh 'pip install unittest-xml-reporting'

                sh 'python Lab4/Test_main.py' 
            }
            post {
                always {
                    junit 'Lab4/test-reports.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }
        }
        stage('Build Docker Image') {
            agent any
            steps {
                script {
                    def imageName = "antonbessarab/programing_technology:${env.BUILD_NUMBER}"
                    sh "docker build -t ${imageName} -f Lab4/Dockerfile Lab4"
                }
            }
        }
        stage('Push Docker Image') {
            agent any
            steps {
                script {
                    def imageName = "antonbessarab/programing_technology:${env.BUILD_NUMBER}"
                    withCredentials([usernamePassword(credentialsId: 'docker_hub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                        sh "docker push ${imageName}"
                    }
                }
            }
        }
    } 
}