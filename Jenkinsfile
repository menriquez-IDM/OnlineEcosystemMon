podTemplate(
    //Docs Build
    podRetention : onFailure(),
    activeDeadlineSeconds : 3600,
    containers: [
        containerTemplate(
            name: 'slurm-container-310',
            image: 'docker-production.packages.idmod.org/idmtools-slurm/idmtools-slurm-python-310:latest',
            command: 'sleep',
            args: '30d'
        ),
  ]) {
  node(POD_LABEL) {
    container('slurm-container-310'){
		def build_ok = true
		def create_bug = false
		def send_to = ''
		def subject_line = ''
		
		stage('Cleanup Workspace') {		    
				cleanWs()
				echo "Cleaned Up Workspace For Project"
		}
		stage('Code Checkout') {
			echo "Running on ${env.BRANCH_NAME} branch"
			git branch: "email_incorporation",
			credentialsId: '704061ca-54ca-4aec-b5ce-ddc7e9eab0f2',
			url: 'git@github.com:menriquez-IDM/OnlineEcosystemMon.git'
		}

		stage('Setup UI Test Environment') {
		    sh 'cd tests'
			sh 'python3 -m pip install --upgrade pip'
			sh 'pip3 install -r requirements.txt'
			sh 'python3 -m pip install --upgrade setuptools'
			sh 'pip install setuptools wheel'
			sh 'python setup.py sdist bdist_wheel'
			sh 'pip install -e .'
			sh 'pip3 freeze'
		}
		stage('Install Driver'){
          sh 'wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -'
          sh 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
          sh 'apt-get -y update'
          sh 'apt-get install -y google-chrome-stable'
          sh 'apt-get install -yqq unzip'
          sh 'wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip'
          sh 'unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/'
          sh '''
              echo VERSIONS------------------------
              google-chrome-stable --version
              chromedriver --version
              '''
        sh 'ls -l'
        sh 'export PATH="/usr/local/bin/chromedriver:$PATH"'
        sh 'printenv PATH'

		}
		// stage('Run Test') {
		//     sh 'python tests/CCWebservice/Test_ccwebservice.py'
    //     sh 'ls -l'
		// }

		try {
    		stage('Run Test') {
    		    sh 'ls -a'
    			sh 'python3 tests/LeakyVaccine/Test_LeakyVaccine.py'
    			sh 'python3 tests/GeneDriveSite/Test_GeneDrive.py'
    			sh 'python3 tests/SFPET/Test_sfpet.py'
    			sh 'python3 tests/CCWebservice/Test_ccwebservice.py'
    		}
		} catch(e) {
		    build_ok = false
		    create_bug = true
		    echo e.toString()
		}
		
//		if(create_bug){
		if(true){
    		stage('Install gh')
    		{
    		    sh '''
    		    type -p curl >/dev/null || ( apt update &&  apt install curl -y)
                curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg |  dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
                &&  chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
                && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" |  tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
                &&  apt update \
                &&  apt install gh -y
                '''
    		}
    		stage('Create issue'){
        	    withCredentials(
                  [usernamePassword(
                    credentialsId: 'e9d44acc-f790-425d-93e9-9dd54cf80ca3', 
                    passwordVariable: 'GH_TOKEN', 
                    usernameVariable: 'GH_USERNAME'
                  )]) {

                    sh '''
                        git config --global --add safe.directory /home/jenkins/agent/workspace/menriquez/LiveSitesMonitoringNightly
                        for f in $(find . -type f -name "*.log")
                        do
                          printf "Tryng to log ISSUE...  $f"  
                          if gh issue list --state "open" --search "$f" | grep -q "$f"; then
                            echo "Bug with title '$f' already exists."
                          else
                            # Create the bug
                            gh issue create --title $f --body-file $f --assignee @me
                            echo "Bug with title '$f' created successfully."
                          fi
                        done
                    '''
                }
    		}
		}


        email_files = sh(script: 'find . -type f -name "*email.txt"', returnStdout: true).split() 
        def email_lines = readFile(email_files[0]).split('\n')
        for (int i = 0; i < email_files.size(); i++) {
            stage ("Emailing Issue ${i} ") {

                send_to = email_lines[0]
                subject_line = email_lines[2]
                echo "Sending email to...   ${send_to}"
                emailext (to: "${send_to}", 
                            subject: "${subject_line}",
                            body: "Assigned to: ${ readFile(email_files[i])}",
                            mimeType: 'text/html');
            }
        }
    }
  }
}

