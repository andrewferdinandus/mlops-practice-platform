# MLOps අවශ්‍ය වෙන්නේ ඇයි?

Machine Learning project එකක් model එකක් train කළාම ඉවර වෙන්නේ නැහැ.

Real-world system එකක model එකක් use කරන්න නම් model එක track කරන්න, save කරන්න, test කරන්න, serve කරන්න, monitor කරන්න, update කරන්න, සහ අවශ්‍ය නම් rollback කරන්න වෙනවා.

MLOps කියන්නේ මේ සම්පූර්ණ lifecycle එක manage කරන්න භාවිතා කරන practices සහ tools එකතුවක්.

## Simple Example එකක්

ඔබ house price prediction model එකක් train කරනවා කියලා හිතන්න.

Model එකට input දෙන values:

    bedrooms = 3
    bathrooms = 2
    location = Colombo
    size = 1200 sqft

Model එක output දෙනවා:

    predicted price = 35,000,000 LKR

Training notebook එකේ මේක වැඩ කරනවා.

නමුත් real-world වලට ගියාම ප්‍රශ්න කිහිපයක් එනවා.

## Problem 1: හොඳම model එක මොකක්ද?

ඔබ model versions කිහිපයක් train කළා කියලා හිතන්න.

    Model A accuracy = 82%
    Model B accuracy = 87%
    Model C accuracy = 79%

දැන් ප්‍රශ්න එනවා:

    හොඳම model එක මොකක්ද?
    ඒ model එක train කළේ මොන parameters වලින්ද?
    ඒ result එක නැවත reproduce කරන්න පුළුවන්ද?
    trained model file එක කොහෙද?

Notebook එකක manually notes තියාගත්තොත් මේක ඉක්මනින් messy වෙනවා.

මෙතනදී experiment tracking වැදගත් වෙනවා.

Experiment tracking වලින් training run එකකට අදාළ details save කරගන්න පුළුවන්.

Examples:

    parameters
    metrics
    artifacts
    training runs

## Problem 2: Model file එක කොහෙද?

Training කරලා model file එකක් save කරනවා කියලා හිතන්න.

    model.pkl

Experiments කිහිපයක් train කළාට පස්සේ folder එක මෙහෙම වෙන්න පුළුවන්:

    model.pkl
    model_final.pkl
    model_final_new.pkl
    best_model.pkl
    best_model_really_final.pkl

මේක real project එකක risky.

හරි model file එක මොකක්ද කියලා පස්සේ හඳුනාගන්න අමාරු වෙනවා.

Model file එකක් artifact එකක්.

Artifact කියන්නේ training process එකෙන් generate වෙන output එකක්.

Examples:

    trained model file
    plots
    metrics report
    prediction output
    data validation report

Good artifact management එකෙන් correct model එක පසුව හොයාගන්න ලේසි වෙනවා.

## Problem 3: වෙන කෙනෙක්ට model එක run කරන්න පුළුවන්ද?

ඔබගේ laptop එකේ training script එක හොඳට වැඩ කරනවා.

නමුත් teammate කෙනෙක් run කරනකොට error එකක් එන්න පුළුවන්.

Possible reasons:

    Python version වෙනස්
    library versions වෙනස්
    missing dependency
    different file path
    environment variable missing

මේ නිසා reproducible environment එකක් අවශ්‍ය වෙනවා.

Docker වගේ tools code එක සහ dependencies package කරන්න උදව් කරනවා. එවිට workflow එක වෙන machine එකකත් එකම විදිහට run කරන්න ලේසි වෙනවා.

## Problem 4: Application එකට model එක use කරන්න ඕනේ

Trained model එක notebook එකක විතරක් තියෙනවා නම් real application එකකට use කරන්න අමාරුයි.

Real application එකක workflow එක මෙහෙම වෙන්න පුළුවන්:

    User website එකක house details enter කරනවා.
    Backend service එක ඒ details model එකට යවනවා.
    Model එක predicted price එක return කරනවා.
    Website එක result එක userට පෙන්වනවා.

මේකට model serving කියලා කියනවා.

Common approach එකක් තමයි model එක API එකක් විදිහට expose කිරීම.

FastAPI වගේ tool එකක් භාවිතා කරලා simple model API එකක් build කරන්න පුළුවන්.

## Problem 5: Production data වෙනස් වෙන්න පුළුවන්

Model එක January data වලින් train කළා කියලා හිතන්න.

නමුත් June වෙද්දී real-world data වෙනස් වෙලා තිබිය හැක.

Examples:

    house prices වෙනස් වෙලා
    user behavior වෙනස් වෙලා
    input data patterns වෙනස් වෙලා

මේකට data drift කියලා කියනවා.

Data drift නිසා model performance අඩු වෙන්න පුළුවන්.

MLOps workflow එකක monitoring සහ drift detection තිබුණොත් data වෙනස් වෙලාද කියලා හඳුනාගන්න පුළුවන්.

## Problem 6: New model එක safely release කරන්න ඕනේ

New model එකක් train කළා කියලා හිතන්න.

Testing වලදී ඒක old model එකට වඩා හොඳයි කියලා පේනවා.

නමුත් production system එකේ old model එක එකවර replace කරන එක risky වෙන්න පුළුවන්.

Safer release process එකක් මෙහෙම වෙන්න පුළුවන්:

    new model එක test කරනවා
    metrics compare කරනවා
    result එක review කරනවා
    small user group එකකට release කරනවා
    behavior monitor කරනවා
    problem එකක් තිබුණොත් rollback කරනවා

මේක model deployment සහ release management වල කොටසක්.

## MLOps කියන්නේ මොකක්ද?

සරලව:

    MLOps = Machine Learning + Software Engineering + DevOps practices

MLOps වලින් machine learning models experiments වලින් real-world systems වලට reliable විදිහට ගෙනියන්න උදව් වෙනවා.

## MLOps විසඳන ප්‍රශ්න

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

## Simple Summary

Machine Learning model එකක් train කිරීම පළමු step එක විතරයි.

Real-world system එකකට model එකක් use කරන්න නම් පහත දේවල් අවශ්‍යයි:

    experiments track කරන්න
    artifacts save කරන්න
    versions manage කරන්න
    predictions serve කරන්න
    behavior monitor කරන්න
    models update කරන්න
    resources cleanup කරන්න

MLOps practices සහ tools මේ full lifecycle එක manage කරන්න උදව් කරනවා.

## Next Note

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
