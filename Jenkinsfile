podTemplate(
    //Docs Build
    podRetention : onFailure(),
    activeDeadlineSeconds : 3600,
    containers: [
        containerTemplate(
            name: 'dtk-rpm-builder', 
            image: 'docker-production.packages.idmod.org/idm/dtk-rpm-builder:0.1',
            command: 'sleep', 
            args: '30d'
            )
  ]) {
  node(POD_LABEL) {
    container('dtk-rpm-builder'){
			def build_ok = true
			stage('Cleanup Workspace') {		    
				cleanWs()
				echo "Cleaned Up Workspace For Project"
			}
			stage('Prepare') {
				sh 'python3 -m pip install --upgrade pip'
				sh "pip3 install wheel"
				sh 'python3 -m pip install --upgrade setuptools'
				sh 'pip3 install -r requirements.txt'
				sh 'pip3 freeze'
			}
		stage('Code Checkout') {
			echo "Running on ${env.BRANCH_NAME} branch"
			git branch: "${env.BRANCH_NAME}",
			credentialsId: '704061ca-54ca-4aec-b5ce-ddc7e9eab0f2',
			url: 'git@github.com:InstituteforDiseaseModeling/OnlineEcosystemMon.git'

			if (env.CHANGE_ID) {
			 	echo "I execute on the pull request ${env.CHANGE_ID}"
			 	checkout([$class: 'GitSCM',
			 	branches: [[name: "pr/${env.CHANGE_ID}/head"]],
			 	doGenerateSubmoduleConfigurations: false,
			 	extensions: [],
			 	gitTool: 'Default',
			 	submoduleCfg: [],
			 	userRemoteConfigs: [[refspec: '+refs/pull/*:refs/remotes/origin/pr/*', credentialsId: '704061ca-54ca-4aec-b5ce-ddc7e9eab0f2', url: 'git@github.com:InstituteforDiseaseModeling/OnlineEcosystemMon.git']]])
			} else {
			 	echo "Running on ${env.BRANCH_NAME} branch"
			 	git branch: "${env.BRANCH_NAME}",
			 	credentialsId: '704061ca-54ca-4aec-b5ce-ddc7e9eab0f2',
			 	url: 'git@github.com:InstituteforDiseaseModeling/OnlineEcosystemMon.git'
			}
		}
		stage('Run Test') {
			sh 'python3 -m pip install --upgrade pip'
			sh 'pip3 install -r requirements.txt'
			sh 'python3 -m pip install --upgrade setuptools'
			sh 'pip3 freeze'
			sh 'python3 -m unittest discover -s tests -p "*Test_.py"'
		}
		

	}
 }
}