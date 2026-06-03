# MLOps අවශ්‍ය වෙන්නේ ඇයි?

Machine Learning project එකක් model එකක් train කළාම ඉවර වෙන්නේ නැහැ.

Real-world system එකක model එකක් use කරන්න නම් තවත් ගොඩක් දේවල් manage කරන්න වෙනවා.

## Simple Example එකක්

ඔබ house price prediction model එකක් train කරනවා කියලා හිතන්න.

Model එකට input දෙනවා:

```text
bedrooms = 3
bathrooms = 2
location = Colombo
size = 1200 sqft
Model එක output දෙනවා:

predicted price = 35,000,000 LKR

Training notebook එකේ මේක වැඩ කරනවා.

නමුත් real-world වලට ගියාම ප්‍රශ්න එනවා.

Problem 1: හොඳම model එක මොකක්ද?

ඔබ model versions කිහිපයක් train කළා කියලා හිතන්න.

Model A accuracy = 82%
Model B accuracy = 87%
Model C accuracy = 79%

දැන් ප්‍රශ්නය:

හොඳම model එක මොකක්ද?
ඒ model එක train කළේ මොන parameters වලින්ද?
ඒ result එක නැවත reproduce කරන්න පුළුවන්ද?

Notebook එකක manually notes තියාගත්තොත් මේක ඉක්මනින් messy වෙනවා.

මෙහිදී experiment tracking අවශ්‍ය වෙනවා.

Problem 2: Model file එක කොහෙද?

Training කරලා model file එක save කරනවා.

model.pkl

නමුත් versions වැඩි උනාම මෙහෙම වෙන්න පුළුවන්:

model.pkl
model_final.pkl
model_final_new.pkl
best_model.pkl
best_model_really_final.pkl

මේක real project එකක dangerous.

Model artifacts properly manage කරන්න ඕනේ.

Artifact කියන්නේ training process එකෙන් generate වෙන output එකක්.

Examples:

trained model file
plots
metrics report
prediction output
data validation report
Problem 3: වෙන කෙනෙක්ට model එක run කරන්න පුළුවන්ද?

ඔබගේ laptop එකේ model එක වැඩ කරනවා.

නමුත් teammate කෙනෙක් run කරනකොට error එකක් එනවා.

Possible reasons:

Python version වෙනස්
library versions වෙනස්
missing dependency
different file path
environment variable missing

මේක solve කරන්න reproducible environment එකක් අවශ්‍ය වෙනවා.

Docker වගේ tools මෙතනදී වැදගත් වෙනවා.

Problem 4: Application එකට model එක use කරන්න ඕනේ

Model එක train කිරීමෙන් පස්සේ application එකකට predictions අවශ්‍ය වෙනවා.

උදාහරණයක්:

Website එකක user house details enter කරනවා.
Backend service එක model එක call කරනවා.
Model එක predicted price return කරනවා.

මේකට model serving අවශ්‍ය වෙනවා.

Common approach එකක් තමයි model එක API එකක් විදිහට expose කිරීම.

FastAPI වගේ tool එකක් use කරලා මේක practice කරන්න පුළුවන්.

Problem 5: Production data වෙනස් වෙන්න පුළුවන්

Model එක January data වලින් train කළා කියලා හිතන්න.

නමුත් June වෙද්දී market එක වෙනස් වෙලා.

House prices වෙනස් වෙලා.
User behavior වෙනස් වෙලා.
Input data pattern එක වෙනස් වෙලා.

මේක data drift කියලා කියනවා.

Data drift නිසා model performance අඩු වෙන්න පුළුවන්.

එහෙම වෙනවද කියලා monitor කරන්න MLOps workflow එකක් අවශ්‍යයි.

Problem 6: New model එක safely deploy කරන්න ඕනේ

New model එකක් train කළා කියලා හිතන්න.

ඒක old model එකට වඩා හොඳයි කියලා පේනවා.

නමුත් production system එකට එකවර replace කළොත් risk එකක් තියෙනවා.

ඒ නිසා deployment process එකක් අවශ්‍යයි.

Good deployment workflow එකකදී:

new model test කරනවා
metrics compare කරනවා
approval ගන්නවා
small traffic එකකට release කරනවා
problem එකක් තිබුණොත් rollback කරනවා
එහෙනම් MLOps කියන්නේ මොකක්ද?

සරලව:

MLOps = Machine Learning + Software Engineering + DevOps practices

MLOps වලින් machine learning models real-world systems වල safely, repeatably, and reliably use කරන්න උදව් වෙනවා.

MLOps විසඳන ප්‍රශ්න

MLOps helps with:

experiment tracking
model versioning
artifact management
reproducible training
model serving
monitoring
data drift detection
deployment
rollback
automation
Simple Summary

Machine Learning model එකක් train කිරීම පළමු step එක විතරයි.

Real-world වලට model එකක් යන්න නම් පහත දේවල් අවශ්‍යයි:

track කරන්න
save කරන්න
version කරන්න
serve කරන්න
monitor කරන්න
update කරන්න
cleanup කරන්න

මෙම problems solve කරන්න MLOps භාවිතා කරනවා.

Next Note

Next note එකෙන් MLOps core concepts explain කරනවා:

experiment
run
parameter
metric
artifact
model registry
pipeline
deployment
monitoring
drift

