Some general questions:
## Why Amazon?
1. Best cloud services with strong customer focus.

2. I can help.

3.  insist on highest standard

4. I have been a user. It would be a dream to work on the cutting edge cloud computing technologies.

5. talented people.



## My Stories
### CMS: Tags (Customer Obsession|Ownership)
S: CMS -> Special feature: tagging

T: Implement the tagging service. They don't have a specific requirement/design on this feature.

A: Designed, implemented a first version. And deliver to them for reviewing. Had a couple follow up meetings gathering feedbacks 
and completed the design + implementation with the content team.

R: They love the final version and is pleased with the tagging feature.

### CMS (invent | dive deep):
S: Video processing includes uploading/compression/encryption, it often happens that there are failure in any of those steps

T: Improve the process.

A: Split it into micro-services using lambda (upload/compression/encryption).

R: Failure rate dropped. Easier re-do. Allows manual operation (S3 bucket event trigger). Collegues really liked the solution.

### CMS:
S: Select from Google drive and upload to S3, no examples online, the solution was to download it to server's FS and upload to 
S3 (Remove the file right after). Broken down when there are quite a bit concurrent users + the file is too large.

T: Research for optimization.

A: Streaming API from google drive and streaming uploading API for S3. 
Found a streaming solution in NodeJS PassThrough stream that pipes source stream to output stream. 

R: Worked really well, with similar or slightly better speed improvement and a huge disk usage improvement (concurrency/file size is no longer an issue).

### CMS:
S: Video url will expire (max 7 days).
T: 
### CMS: Slow (Dive deep|Customer Obsession|Invent Simplify|Learn and be curious)
S: CMS slow loading time, asset editing was laggy.
T: Speed it up. Couple solutions provided by coworkers, not very ideal (complicated -> a big amount of changes needed to the codebase).
A: My experience on frontend is limited. Then I did some research on performance improvement and UI/UX improvement. 
New tech -> React virtualized (windowing technology), Study the documents, apply it. Also added a few UI improvement (such as adding loading bar and stuff)
Added server cache.
R: Speed was improved a lot, the loading, asset editing, clicking were all improved. Minimum code changes. Customers are happy.

### Math Tutor (Customer Obsession|Bias for Action): 
S: Math tutor -> demo on the prototype of future product
T: Task -> Deliver this with my coworkers. 2 Weeks DDL, missed the DDL because need more time imporving the performance.
A: As soon as I realized the DDL was not achievable, I communicate with the manager, acknowledge my misjudgement on the time and offered 2 plans. One is cutoff 
R: They took the second plan, and we are able to meet the DDL.

### Python tutorial for using the .so file (Ownership | Think big | Learn to be curious)
S: Cross-platform cross language SDK. Limited resources, original plan was to provided a .so with tutorial (python).
T: Write python tutorial.
A: Learn a new tool/library called pybind (C++ code to python directly). Packaging it with pip wheel file. 
R: Manager is impressed by what I finally delivered.


