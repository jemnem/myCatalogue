node ('api-test') {
    stage('Get the code from githut') {
       git credentialsId: 'b6b44b1f-71e5-49b9-89b6-fb29ae993b4e', url: 'https://github.com/jemnem/myCatalogue.git'
    }
    stage('Deploy') {
        echo 'start deploying...'
        sh 'docker-compose stop'
        sh 'docker-compose rm -f'
        sh 'docker pull python'
        sh 'docker run -v ${PWD}/test:/usr/src/test  -w /usr/src/test python python sqlGenerator.py'
        sh 'cp ${PWD}/test/data/dump1.sql ${PWD}/docker/catalogue-db/data/'
        sh 'docker-compose build --no-cache'
        sh 'docker-compose up -d'
        sleep 30
    }
    stage('Test') {
        echo ' start testing...'
        sh 'docker pull postman/newman_ubuntu1404'
        try {
            sh 'docker run -v ${PWD}/test:/etc/newman -t postman/newman_ubuntu1404 run catalogue.postman_collection.json -e catalogue.postman_environment.json --color off'
        }
        catch (e) {
            echo 'rollback the service to the last good one'
        }

    }
}

