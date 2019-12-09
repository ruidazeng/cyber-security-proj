# cyber-security-proj
Final Project for CS 3891 Special Topics: Cyber Security at Vanderbilt University with Professor Jules White

# Name: Ruida Zeng
# VUnetID: zengr
# Email: ruida.zeng@vanderbilt.edu
# Class: CS 3891 - Special Topics: Cyber Security
# Date: Nov 4, 2019


* What are you trying to do? Articulate your objectives using absolutely no jargon.

I am trying to further secure devices owned by Vanderbilt or is currently on the
Vanderbilt network against potential hackers with malicious intent, whatever those
malicious intents may be. This will be done through Shodan, which is a search engine
that allows users to find devices connected to the Internet that are insecure.
Examples of these devices include routers, switches, along with other miscellaneous
embedded system or Internet of Things (IoT) devices that are on the Vanderbilt
network that may contain default passwords or default configuration that make it
easy for attackers to gain access. The website will crawl through the entire Internet
in search for any publicly accessible devices on the Vanderbilt network. 
These devices, when compromised, could potentially lead to a huge leak that
threatens the the Vanderbilt communities through privilege escalation;
it might also lead to a much worse situation that have yet to be imagined.


* How is it done today, and what are the limits of current practice?

Currently, the vulnerability scan is simply not being done by VUIT as they are
often times already occupied with hundreds of other tasks such as maintaining
the complex yet important authentication system against intrusions, securing
our research databases, managing the financial repository that our Human Resources
Department uses, and most importantly, responding to incidents that are happening
on a daily basis that are potentially detrimental to Vanderbilt's network and IT
infrastructures. Simply put, there is just not enough priority tag put on this
objective by VUIT, although according to Masood, this is indeed something they
would like to have in the near future.


* What is new in your approach and why do you think it will be successful?

Ironically, there is nothing new in my approach as it has never been done before
due to the fact that there is just not enough priority tag placed upon my objective
by VUIT despite the fact that this is indeed something they would like to have
in the near future at VUIT. I think it will be successful for two reasons, that
this project is something that I know for sure I could do in conjunction with
VUIT that does not require either (1) elevated access which could take a tremendous
amount of time to obtain, or (2) extensive knowledge about the infrastructure
and the systems that are currently in place as it only requires knowing how to make
API calls to the shodan server and knowing how to visualize the results returned.
According to Masood, this will not be a difficult project to accomplish and
will take an individual no longer than 3 weeks to complete.


* Who cares? If you are successful, what difference will it make?

This project will further strengthen the IT infrastructure of Vanderbilt University
while also enhances the protection that Vanderbilt students, staffs, and faculties
receive against external threat from attackers with extremely malicious intents.
As Vanderbilt continues to grow both in terms of reputation in academia (which
could mean the existence of some very valuable research work in areas such as
medical and engineering) and in terms of expansion of physical infrastructure,
it is inevitable that we will attract the attention of malicious attackers with
nefarious intents. Being able to strengthen the IT infrastructure, especially
that of the embedded systems that we currently use, we could secure ourselves
against these attacks that could lead to severe damages. Because if the attackers
could gain access to low value devices that often times have the least privilege,
they could use that weakest link as a leverage point and create potentially more
detrimental attacks. Although this might be a stretch, it could potentially provide
serious and dangerous attacks such as "unlocking doors to residential halls or
labs that the attackers have no authorization to access" or "using private
videos that the security cameras accidentally capture for leverage or ransom".


* What are the risks?

After a conversation with Masood Sidiqyar, there is little to no risk as I will
not need special permission from the Vanderbilt bureaucrat nor would I need elevated
access in order to perform vulnerability assessment using shodan because shodan
contains information that is publicly available to anyone on the Internet anyway,
and all I am doing is retrieving what is publicly available about Vanderbilt
devices and visualizing them.


* How much will it cost? If your approach isn't free, think
carefully about the cost to use or implement what you propose.

My approach is free as long as I strictly adhere to the API calls limit that
shodan impose daily. This also means I have to maximize efficiency when going
through the testing phrase of my project in order to minimize the API calls
made to the shodan server. I have yet to estimate the difficulty of strictly
adhering to the API calls limit. However, worst case scenario, I might end up
purchasing the "Freelancer" package offered that cost $59 per month which allow
for up to 1 million results per month and scan up to 5,120 IPs with network
monitoring and extensive filtering with an added paging features. Again, I am
well aware that $59 is a significant cost but if it will significantly improve
the security at Vanderbilt it will be a worthwhile investment to make. However,
as a thrifty person, I will still try to mitigate and avoid the cost if possible.


* How long will it take?

It will most likely take 2-3 weeks to accomplish simply due to the fact that
this project will not be trivial and will require many API calls made to the
shodan server. And as we know, API calls are usually not free and often times
have an upper bound, the testing of the program will likely need to be done
over a period of a few days.


* What are the mid-term and final “exams” to check for success?

My goal is to finish my code bases for making API calls for the shodan and begin
the testing phrase by the midterm point. The final project should be able to
successfully visualize the results using generated charts and graphs in a way
that can be easily understood and put to effective usage by the people that work
at VUIT such as Masood Sidiqyar. The final visualization should be done in a way
that actually contributes to VUIT's operations in a meaningful way such as
determining which vulnerability are much more important and detrimental in
comparison to the others.
