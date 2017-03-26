git fetch origin
reslog=$(git log HEAD..origin/master --oneline)
if [[ "${reslog}" != "" ]] ; then
	git merge origin/master
python3.6 vision_bot.py