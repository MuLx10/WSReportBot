
<a href="https://slack.com/oauth/authorize?client_id=374384770263.373477440613&scope=commands,bot,chat:write:bot">
<img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" />
</a>

# WSReportBot

## Problem Overview:

In large github projects with so many collaborators, it often happens that many contributors, especially project maintainers come back to contribute to that project, after a long time(due to break and other reasons). So, after that period of time, when they want to track what all changes have been made to that project so far, it becomes really difficult to go through all the notifications and look for changes, if they are keeping a watch on project. Moreover, the contributors, who dedicate their lot of valuable time to make their contributions to the project, should be honored/ recognised for the same in a way in that project community, to make those contributors feel the sense of achievement, and at the same time, motivating more contributors to do the same.

## Idea Overview:
We've built a slack bot for the communication channel of that project/ organisation that will analyze all the changes made to that project, and will generate weekly report, summarizing what all changes were made ( by analyzing merged pull requests and changes made by admin). This will thus help all the contributors and project maintainers to stay up-to-date and keep track of all changes made in that project. Also, this bot will analyze the contributors graph for that project, and will mention top 10 contributors who were most active in that week with changes they made. This will thus help in highlighting those contributors in that project community, and at the same time saves the time of project admin, by reducing the efforts of keeping a regular check of contributions graph.

## Features and Hasura APIs used
1. We’ve built login associated with different organization using Hasura Auth API.
2. For each organization its associated repository contributions are stored in database using Hasura Database API.
3. **Weekly summary or report for all the changes made** : It’ll contain list of all the changes made to that project per week. This will be done by analyzing all the pull requests merged in that week along with changes made by project admin.
4. **Weekly report on top contributors and recognising their contributions in community channel** : Weekly report would be generated containing list of all the contributors, appreciating the significant contributions they made. This will highlight them in the community, making them feel a sense of achievement. This will thus increase the community involvement of more users and motivate more users to do the same. This automation work will help project admin also to keep track of all the contributors and contributions, thus saving their lot of time. The app will be integrated with the channel. 

