#!/bin/bash
function auditSRV(){
declare -A app_
app_["ffmpeg"]="ffmpeg, piller"
app_["curl"]="curl, admin"
for key in ${!app_[@]}; do
if which ${key} >/dev/null; then
	echo "YES - app - ${app_[$key]}"
else
	echo "NO  - app - ${app_[$key]}"
fi
done
declare -A fi_
fi_["$ww/widgets/python/vps-hoth-7facG-file-links.py"]="VPS"
for key in ${!fi_[@]}; do
if [ -f "${key}" ]; then
	echo "YES - .py - ${fi_[$key]}"
else
	echo "NO  - .py - ${fi_[$key]}"
fi
done
}
declare -A fo_
fo_["/home/admin/domains/eyeformeta.com"]="eyeformeta.com"
fo_["/home/admin/domains/911.alexandria.ninja"]="911.alexandria.ninja"
fo_["/home/admin/domains/alexandria.ninja"]="alexandria.ninja"
fo_["/home/admin/domains/apps.eyeformeta.com"]="apps.eyeformeta.com"
fo_["/home/admin/domains/bespin.eyeformeta.com"]="bespin.eyeformeta.com"
fo_["/home/admin/domains/ext.eyeformeta.com"]="ext.eyeformeta.com"
fo_["/home/admin/domains/eyeformeta.com"]="eyeformeta.com"
fo_["/home/admin/domains/hashtable.info"]="hashtable.info"
fo_["/home/admin/domains/i4meta.com"]="i4meta.com"
fo_["/home/admin/domains/load.eyeformeta.com"]="load.eyeformeta.com"
fo_["/home/admin/domains/m-eta.app"]="m-eta.app"
fo_["/home/admin/domains/meta.eyeformeta.com"]="meta.eyeformeta.com"
fo_["/home/admin/domains/rephrecruiting.com"]="rephrecruiting.com"
fo_["/home/admin/domains/stark-minecraft.com"]="stark-minecraft.com"
fo_["/home/admin/domains/xan.guru"]="xan.guru"
fo_["/home/admin/domains/youtube.eyeformeta.com"]="youtube.eyeformeta.com"
site_y_=()
site_n_=()
for key in ${!fo_[@]}; do
if [ -d "${key}" ]; then
	site_y_[${#site_y_[@]}]=${fo_[$key]}

	# echo "YES - site - ${fo_[$key]}"
else
	site_n_[${#site_y_[@]}]=${fo_[$key]}
	# echo "NO  - site - ${fo_[$key]}"
fi
done
for val in "${site_y_[@]}"
do
if curl -s --head  --request GET https://${val} | grep "200" > /dev/null; then 
	echo "HAS - UP - site - ${val}"
else
	echo "HAS - DN - site - ${val}"
fi
done
for val in "${site_n_[@]}"
do
	echo "NO  - site - ${val}"
done
auditSRV