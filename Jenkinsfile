pipeline {
    // Додає мітки часу до логів для кожного кроку
    options { timestamps() }

    // Вказує, що агент не використовується глобально
    agent none

    // Налаштовує змінну середовища з обліковими даними Docker
    environment {
        DOCKER_CREDI = credentials('docker') // Ім'я "docker" має співпадати з існуючим налаштуванням
    }

    stages {
        // Стадія перевірки вихідного коду
        stage('Check scm') {
            agent any
            steps {
                // Отримує код з репозиторію
                checkout scm
            }
        }

        // Стадія збірки
        stage('Build') {
            steps {
                // Виводить номер білду та повідомлення про завершення збірки
                echo "Building ... ${BUILD_NUMBER}"
                echo "Build completed"
            }
        }

        // Стадія тестування
        stage('Test') {
            // Використовує Docker-образ Alpine як агент
            agent {
                docker {
                    image 'alpine'
                    args '-u="root"'
                }
            }
            steps {
                // Встановлює Python і pip
                sh 'apk add --update python3 py3-pip'
                // Створює віртуальне середовище Python
                sh 'python3 -m venv /venv'
                // Активує середовище та встановлює unittest-xml-reporting
                sh 'source /venv/bin/activate && pip install unittest-xml-reporting'
                // Запускає файл з тестами
                sh 'source /venv/bin/activate && python3 test_notebook.py'
            }
            post {
                // Завжди зберігає результати тестів
                always {
                    junit 'test-reports/*.xml'
                }
                // Виводить повідомлення при успішному тестуванні
                success {
                    echo "Testing successful"
                }
                // Виводить повідомлення при невдалій перевірці
                failure {
                    echo "Tests failed"
                }
            }
        }

        // Стадія входу в Docker і пушу образу
        stage('Docker Login') {
            agent any
            steps {
                script {
                    // Виконує логін у Docker, використовуючи збережені облікові дані
                    sh "echo $DOCKER_CREDI_PSW | docker login --username $DOCKER_CREDI_USR --password-stdin"
                    // Збирає Docker-образ і пушить його до Docker Hub
                    sh "docker build -t sergoo/lab4-jenkins:${BUILD_NUMBER} --push ."
                }
            }
            post {
                // Завжди виходить з Docker після завершення
                always {
                    sh 'docker logout'
                }
            }
        }
    }
}
