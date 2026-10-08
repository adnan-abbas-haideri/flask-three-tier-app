pipeline {
    agent any

    environment {
        SONAR_HOME = tool 'Sonar'
    }

    stages {
        stage('Code') {
            steps {
                git url: 'https://github.com/adnan-abbas-haideri/flask-three-tier-app.git',
                    branch: 'main'

                echo 'Code Clone Successful'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Sonar') {
                    sh '''
                        "$SONAR_HOME/bin/sonar-scanner" \
                        -Dsonar.projectName=flask-three-tier \
                        -Dsonar.projectKey=flask-three-tier
                    '''
                }
            }
        }

        stage('SonarQube Quality Gates') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: false
                }
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                withCredentials([
                    string(
                        credentialsId: 'NVD-API-KEY',  
                        variable: 'NVD_KEY'           
                    )
                ]) {
                    dependencyCheck(
                        odcInstallation: 'OWASP',
                        additionalArguments: "--scan ./ --format XML --nvdApiKey ${NVD_KEY}"
                    )
                }

                dependencyCheckPublisher(
                    pattern: '**/dependency-check-report.xml'
                )

                echo 'OWASP Dependency-Check Report generated'
            }
        }

        stage('Build & Test') {
            steps {
                sh 'docker build -t flask-app:latest .'

                echo 'Docker Image Built Successfully'
            }
        }

        stage('Trivy') {
            steps {
                sh 'trivy image flask-app:latest'

                echo 'Image scanned'
            }
        }

        stage('Push To Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'DockerHubCred',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh 'docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"'
                    sh 'docker tag flask-app:latest "$DOCKER_USERNAME"/flask.jenkins'
                    sh 'docker push ""$DOCKER_USERNAME"/flask.jenkins"'
                    
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose down && docker compose up -d'

                echo 'Container deployed successfully'

            }
        }
    }
}
