# Fighting the Forever War:  Trust and Safety Engineering

By Alex Stamos and Shelby Grossman

with Riana Pfefferkorn and Adriana Stephan

### Reading Note:

* This book manuscript is a rough draft under continuous improvement.   
* It was initially written over several years from 2019-2025 and has been updated as technologies and situations have changed. As a result some companies are referred to by their prior name, and the manuscript does not fully reflect the role of AI in trust and safety concerns and solutions. Additionally, there are some formatting inconsistencies, including in captions and references.  
* We are posting this book now so that we may use it to teach our Trust & Safety course at Stanford and to get feedback from our students and others.  
* This book benefits from the many guest speakers at my Trust & Safety class at Stanford. These include Nelly Agbogu, Vic Baines, Brian Fishman, Karen Maxim, Casey Newton, Yemi Ogundare, Brenna Smith, Anna Van Meter, and Sean Zadig. Any errors are the responsibility of the authors and not the guest speakers.  
* We welcome feedback on this book manuscript. Email us with corrections or other feedback at feedback@tsbook.org. You are also welcome to file an issue in Github or to submit a pull request. If you submit a pull request you are explicitly assigning your copyright to the authors so that we can continue to publish this book under Creative Commons and perhaps put out a paper copy (which will instantly be out-of-date versus the repo, but boy does paper feel nice).  
* While this book has been written as a group project, in situations where the first person “I” is used it comes from the perspective of Alex Stamos and all opinions are his alone. This is mostly a reflection of the fact that Alex has the craziest Trust and Safety anecdotes of this group although the Stanford students (now alumni) who have helped with research are catching up quickly\!  
* Figures and tables without a source noted were created by Alex Stamos, which should be obvious from the lack of artistic merit.

### Preface

The tech industry is facing a crisis of confidence and competence in dealing with the human impact of the products it builds. There are many aspects to that crisis, including privacy violations, security failures and monopolistic practices, but an overriding and systemic issue has been a failure to properly foresee and react to the misuse of new technologies by bad actors. 

There is an entire field dedicated to detecting and stopping the abuse of tech to cause harm, which generally goes under the name “Trust and Safety.” Such teams have existed since the late 1990’s, but there has been a lack of centralization and regularization of knowledge since then. As a result, new companies often face the exact same problems that were first dealt with decades ago, and often are not able to benefit from what has been learned by those who have come before. 

We wrote this book to provide a comprehensive look at the real problems facilitated by modern internet companies from my experience leading teams on the front lines of some of the most difficult technologically facilitated challenges of the 21st century.


I come from a traditional information security (InfoSec) background. My parents bought me a Commodore 64 when I was eight years old, hooked to a small TV. I was fortunate enough to have the opportunity to attend excellent public schools, concluding with studying Electrical Engineering and Computer Science at UC Berkeley. At the time, security was not a core part of the CS curriculum; the one security class I was able to take was targeted at grad students and taught by Berkeley’s newest assistant professor, David Wagner. But I still caught the bug, working as a security engineer at Loudcloud, @stake, and iSEC partners, a company I founded dedicated to helping others build trustworthy systems. 

When I showed up at Yahoo\! and then Facebook as Chief Information Security Officer, I anticipated spending a majority of my time on traditional InfoSec challenges. However, at companies serving billions of users, I learned that the vast majority of bad things that happen to people online have nothing to do with information security or complex technical problems. There’s a whole host of really horrible things that happen with the help of technologies we build that have no interesting technical component.  It is what we classify as abuse: the technically correct use of the products we build to cause harm, think hate speech, harassment, disinformation, the sexual abuse of children. All of these problems have existed in society in some form for a long time, yet the internet amplified and facilitated new forms of abuse. 

When I left Facebook for Stanford, I committed to educating the next generation of technologists to avoid these mistakes. This book is part of my mission to create a cross-disciplinary space to study and teach trust and safety as a discipline in academia, along with the research of the Stanford Internet Observatory and the Stanford Computer Science course upon which the book is based. Computer science programs now recognize computer security as a core competency for every undergraduate, and companies recognize that security teams are a necessary part of their companies. We hope to establish the study of trust and safety as a standard part of the training of young software engineers and to help new companies reduce their negative impact on the world. Since starting our course, hundreds of our alumni have gone on to work in the tech industry, civil society and government and dozens of other universities have also offered similar courses, many using the content of the Trust and Safety Teaching Consortium our team incubated[^1]. 

There are many books on how tech is destroying our minds, destroying democracy, destroying the world. While most of these books have legitimate grievances, they are generally not informed by a deep understanding of what is actually happening and almost never propose practical solutions. This book will tell the history of how tech companies have learned of and mitigated the most prominent types of online abuse, tell real victims’ stories, and provide practical advice for entrepreneurs, engineers, and policymakers dealing with trust and safety issues for the first time. We also hope to ground policy discussions in real world tradeoffs. 

We dedicate each chapter to a particular type of abuse (e.g. spam, child sexual exploitation, or disinformation). In most chapters we’ve included charts comparing major platform policies on these challenges to help new companies get a head start on keeping users safe online. We also include additional chapters dedicated to describing a particular technical topic that can be used to fight various abuse types (cryptography, machine learning, and adversarial ML). Each chapter can be read independently and the book can be read in non-contiguous fashion.

**This book targets four kinds of readers:**

**Computer Science Students and Professors** \- Our hope is that this book will help inform the creation of trust and safety courses at the undergraduate level across the world. The layout of the book closely follows how we teach our course at Stanford[^2], CS 152/COMM 122/INTLPOL 267: Trust and Safety, and students are welcome to experience the book linearly along with materials from our class or as part of self-study. They also might be interested in using the chapters describing specific abuses as a good roadmap for finding new areas for research or tool development. The technical background chapters will likely constitute a review of basic concepts for most upper division CS students.

**Policymakers and Policy Analysts** \- The regulation of online behavior and the companies that facilitate it are a key topic in many different policy debates ranging from data protection, national security and the struggle against disinformation. We hope that this book helps inform and ground these debates in facts about how various abuses express themselves and the existing systems in tech companies to deal with them. These readers might find the technical background chapters, such as the one on machine learning, to be a good introduction to complicated technical fields and then I expect these readers to be best informed by the specific abuse topics relevant to their policy interests.

**Working Product Managers and Engineers** \- Professionals working in communications or user generated content platforms can use this book as a way to familiarize themselves with the broad range of harms that can arise from such products and the kinds of adversaries they are likely to face. The technical chapters will likely be seen as too simple for working software engineers, but the abuse chapters and the recommendations on team formation in the conclusion are hopefully helpful. 

**Entrepreneurs** \- The best time to think about trust and safety problems is early in the lifecycle of a new platform, and we hope that entrepreneurs use the introduction and conclusion chapters to help them understand the kinds of team members they should recruit and functions they should support. New companies with a specific focus on children or teenagers, such as a social photo app or game platform, should pay close attention to the child safety chapter.

This book captures decades of problems and solutions in one place. We would like entrepreneurs to consider trust and safety issues much earlier in their product design process. We would like venture capitalists, advisors and other people in the startup ecosystem to make consideration of trust and safety challenges a standard part of the expected steps a new company will take. We would like students in computer science programs to consider specializing in trust and safety and putting their skills to use stopping really horrible abuses instead of optimizing ad click-thru rates. And finally, we would like media commentators and politicians to ground their complaints in reality and to be focused on the most harmful abuses of modern communications platforms. 

### Content Warning

The fundamental mission of this book is to shine a light on the greatest harms committed online, and provide necessary guidance on how to fight them effectively. In doing this, the book will describe in detail some of the worst parts of humanity and is aimed for adult readers. While there are warnings before especially hard chapters, like terrorism and child sexual exploitation, different chapters may impact readers in different ways, and the book is designed such that it can be read non-contiguously. Our hope is that by proactively engaging with issues of user harm and understanding how technology facilitates abuses, you can have a direct impact on making the internet a better, safer place.

# Introduction to Trust and Safety

I sat paralyzed on Mark Zuckerberg's couch, staring at my hands, as Sheryl Sandberg dished out the verbal punishment. It was September 8, 2017, and a blog post signed by me had been posted the day before announcing that Facebook had discovered hundreds of fake accounts and about $100,000 in ad spending by the Russian Internet Research Agency (IRA) on Facebook during the 2016 U.S. Presidential Election. 

As the Chief Security Officer at Facebook, just as in my previous role at another public tech company, I had a fiduciary responsibility to the shareholders. And as a practical matter the representative of those shareholders, when it came to risk management, was this Audit Committee. 

Three distinguished and brilliant individuals sat on the Committee at the time. Marc Andreessen[^3], the inventor of the web browser and now one of the most powerful venture capitalists in Silicon Valley. Dr. Sue Desmond Hellman, the former chancellor of UC San Francisco, and at that time, the CEO of the Bill and Melinda Gates Foundation. And most relevantly, Erskine Bowles, the former Chief of Staff to President Bill Clinton. 

The day before my executive-level flogging, I had briefed the Audit Committee on my team's findings just hours before the news was set to break. All three directors were shocked but Bowles, in particular, immediately grasped the significance of these findings. The raucous 2016 election and shocking win by Donald Trump had driven a wedge into American society, and the fact that part of that wedge had been driven by the Russians, using Facebook, was a fact that he knew would become radioactive in the Democratic Party, in Washington, and across the country. 

During that meeting, Mr. Bowles had asked me: “Did you get it all? Is there anything more?” While predictable, this was not a question I was looking forward to answering. Nobody wants to be the person who walks into the room with a problem they identified and half-solved, especially an exec at a tech company where backing your assertions with firm, empirical evidence was close to a religion. I replied to Bowles, who was perhaps using the same stare on me that allowed him to manage up to a famously uncontrollable President, as truthfully as I could. I told the committee that no, I did not think that we had caught all of the activity in 2016 and that there's quite possibly a great deal more examples of government propaganda, lurking somewhere in the exabytes of content that Facebook stored in datacenters around the globe. I explained to them that we were effectively on our own, with Facebook receiving no help from the FBI or other government agencies, and that no other companies had publicly or privately[^4] discussed similar findings. As a result, we had no other set of malicious actions to measure ourselves against, and there was no way to know how much the Russians or any other group had spent on Facebook in 2016\.

It would be an understatement to say that Bowles was not pleased with my answer. That night, during a dinner between the entire Board of Directors, Mark, Sheryl, and other senior executives, Bowles ripped into Mark and Sheryl angrily, especially hammering the fact that my briefing had been the first time the Audit Committee or the Board had been informed of what was at that point a six-month long investigation. The next morning, Sheryl took out this anger on me, telling me that I had betrayed her and Mark, that I had not properly prepared her for what I was going to tell the Board, and that this was my failure, not hers. 

I understood the root causes of Sheryl's frustration. While there is a widespread belief that Sheryl Sandberg was the second most powerful person at Facebook, even in 2017 this was not true. The truth is that there is a whole host of widely anonymous executives, mostly men, who lead up various product and engineering teams and who have earned hundreds of millions of dollars in Facebook restricted stock units as they steered the company from its days as a small dorm room project to the most dominant communication platform on the planet. As the people who decided what was important and not, and who set the metrics by which the product and engineering teams operated, these lesser-known individuals are the ones who actually wielded the secondary power to Mark Zuckerberg, who as the majority vote holder, Chairman of the Board, and CEO, was in the end the God King of the multi-billion user Facebook empire.

These product leaders decided what features Facebook would ship, what regions would be targeted for those features, and how success and failure would be measured and engineers motivated per those metrics. Sheryl, on the other hand, was relegated to cleaning up the mess these men created. As the COO, Sheryl had been assigned the parts of Facebook that Mark Zuckerberg did not consider critical, ranging from HR and financial operations to the legal and policy teams, including me, the rest of information security and the majority of safety teams. She also helmed functions that at other companies would be considered absolutely critical, such as ad sales, but that Mark took little interest in.

Mark, at his core, is a product person. He greatly enjoys thinking about how people will use the products he builds and imagining the positive impacts on individuals and societies. Like most product people, he is an optimist, and does not spend much time thinking of the darker uses of his product or the foibles of humanity that one must deal with when serving billions of users. This turns out not to be a Facebook specific problem, as we will discuss multiple times in this book, **the vast majority of platforms that allow communication between individuals are not built with awareness of the real risks inherent in the complexity and darkness that one finds in human society**. Instead, they are built with the assumption that people are good and that products will be used in exactly the same way as which they are designed. Such thinking started with Mark, but by 2016 had come to permeate Facebook at a fundamental level.

So, while I sat there mortified, taking the tongue lashing from Sheryl as over twenty other Facebookers watched on in person and on the video bridge[^5], I also understood her frustration. That being said, I don't think I deserved to get yelled at either. But that's the reality for those of us who work on understanding and dealing with the dark side of consumer internet products. A reality that we hope to explore in this book as we talk about the development and the future of trust and safety in Silicon Valley and around the world.

## Key Themes

As we explore a wide range of online harms, victims and responses, we will continuously return to some key themes that you might want to look out for: 

1. Almost every harm we discuss in this book is something that predates the internet, and understanding the history of these harms is important if we want to predict and prevent future damage to individuals. 

2. Likewise, understanding the history of online abuses and how various companies have tried (and often failed) to deal with them is critical for any team working on a new product that allows for human interaction.

3. Most platform policies involve difficult trade-offs between legitimate equities. How do you balance the right of political free expression against the desire to prevent disinformation? How do you balance individual privacy rights against the benefit of anti-abuse scanning technologies? 

4. These trade-offs cannot be avoided, but the final optimization can be improved through a deep understanding of the real issues and practical solutions.

5. Tech companies should prioritize their trust and safety work by considering the level of harm associated with an area of abuse, the prevalence of the abuse as well as the responsibility their particular product has for enabling such abuse. This kind of prioritization is better than constantly chasing media and political pressure.

6. It is very common for platforms to spend most of their time on issues that occur in the languages spoken by key executives and in developed countries where there are pressing media and political risks. This means that other serious harms might go unaddressed in the countries where a majority of users reside. 

7. Platforms have legal obligations around data access and some specific abuses (like child exploitation), but the vast majority of decisions they make will require them to create standards that go well beyond what they are legally required to do.

8. It is a constant struggle to balance the desire to use automated systems to scale trust and safety enforcement across a platform against the reality that humans are much better at predicting how other humans will act.

9. Cryptography and machine learning are two of the critical technologies needed to prevent certain types of abuse, but are also paradoxically technologies that can be used to cause harm.

## So what is Trust and Safety?

Trust and Safety is the study of how the technology platforms that facilitate interactions between human beings can be used to cause harm and the steps that can be taken to prevent or mitigate those harms. The term is traditionally used to describe the teams and functions that exist inside of the corporations that own the largest online speech platforms, although as the field expands 

Information security, or as we're likely to call it these days cybersecurity[^6], is the study of how individual individuals break computer systems and force them to do things outside of their original design parameters. In the information security space, we have the idea of the CIA triangle, each corner of the triangle representing something we are trying to protect: confidentiality, integrity, and availability. 

![][image1]

*Figure 1: The CIA triangle. (Source: Wikipedia[^7])*

Russia's interference in 2016 gives us an example of a situation where cybersecurity and trust and safety intersected; while hacking techniques were used as part of the propaganda campaign, those were not part of the arsenal deployed against Facebook itself. The Russian trolls, who created fake accounts pretending to be Americans and then organized those accounts into pressure groups on specific topics of high political interest in the United States, were using Facebook in the exact way it was designed. This is why this type of disinformation or propaganda activity actually falls under a different rubric, one that is often referred to in Silicon Valley as trust and safety. 

One way to differentiate trust and safety is to define it as **preventing the technically correct use of products in a manner that causes harm**. When a hacker breaks into a social media company and convinces its database server to give up private user information, it constitutes an information security problem. In that situation, the hacker is violating the basic controls built into the system and making it perform in a way that the original engineer did not intend and, perhaps, didn't even understand. However, if an attacker sends a message via a social media network that is accurately stored in a database and then causes harm when correctly shown to another user, that is a trust and safety issue. There is no violation of a technical control, the system is working just fine, it just happens to be that the correct usage of the product can be harmful.

While still young compared to other areas of engineering, information security is relatively mature and advanced compared to the trust and safety work we'll discuss in this book. Ever since computers started being connected to one another there have been attempts to violate the security protections of them. One of the best books written about information security actually dates from the 1980s. Cliff Stoll’s *The Cuckoo's Egg* recounts Stoll’s tracking down of Russian hackers in very early computer systems operating at the Lawrence Berkeley National Laboratory in the hills above the University of California campus[^8]. While the technological details in this book seem alien to a modern reader, and he references systems that my students at Stanford have never seen in their lives[^9], the basic ideas behind the violation of those mainframes remain the same. 

One of the challenges with trust and safety is that it does not fall cleanly into any single academic discipline. Information security is mostly a problem of computer science, although there are important parts of psychology and sociology that are involved in issues such as phishing and social engineering of individuals. Trust and safety has no such home as it involves all of the various sins and failures of humanity now reflected in our online lives[^10]. 

Security failures can have serious consequences. A virus can shut down a hospital's network. A SQL injection flaw can be used to steal information of millions. But in all of these cases, the human impact is often indirect and requires several steps by an attacker before a victim is seriously harmed. In the trust and safety field the human impact is often immediate and sometimes much more substantial than the impacts of the vast majority of information security failures. While I took pride in the work that I did to protect companies against attackers, such as the Ministry of State Security of the People's Republic of China or the Russian FSB[^11], I also had to realize that a great deal of harm was accruing to the customers of these companies due to the actions of much more prosaic, but no less evil adversaries.

## Why does Trust and Safety matter?

Information Security and Trust & Safety are professionals united by the shared goal of keeping people safe. That doesn’t mean that they always agree on how to apply their efforts to get the most return-on-investment[^12].

![][image2]

*Figure 2: Triangle of common information security harms.* 

This triangle is from a number of presentations I've given where I've tried to communicate my feelings on the current state of the information security industry and the related subfield of security focused computer science. The triangle is meant to represent by area the amount of InfoSec harm caused by each of these categories of failures. At the bottom of the triangle is account lifecycle/passwords, meaning that in my estimation, by far the largest problem in all of information security is the fact that a username and password, an idea that comes out of 1970s timeshare mainframe architectures, continues to be the primary way in which people authenticate themselves in both personal and professional computing environments. 

As we go up the triangle, we have slightly less common problems, such as all the security flaws caused by a lack of patching, simple configuration errors that one sees when one works professionally in assessing enterprise networks as I have, as well as vulnerabilities and applications that we've known about for decades. The top part of the triangle is labeled new research, meaning the sum impact of all of the interesting new security flaws that have been discovered over the last several years. 

The arrow at the top is meant to point to the absolute top pixel of this triangle which represents the sum total of impact from zero days, meaning vulnerabilities that are brand new, have never been exploited in the wild, and for which there is no patch. Security specialists and vendors love to talk about zero days. But the truth is that the vast majority of successful attack campaigns by even the most advanced cybersecurity actors are conducted without any use of such expensive and valuable tools. The point of this triangle is to demonstrate that the security industry’s[^13] focus on the complexity and sexiness of different types of exploits is misplaced, as that focus does not match up with the day-to-day problems that cause the vast majority of security incidents around the world. 

![][image3]

*Figure 3: The Stamos hierarchy of the actual bad stuff that happens online to real people.* 

But if you zoom out from this triangle, you see this second, much larger pyramid, the vast base of which I have labeled abuse, referring to the technically correct use of a product to cause harm. I've tried to name this triangle the ‘Stamos hierarchy of the actual bad stuff that happens online to real people’ with an eye on my legacy and based on the fact that real academics cannot truly be blessed as such until they have a theorem, process, or in this case PowerPoint art named after them. My serious message is that while information security is important, and those of us who have dedicated our lives to it have committed to a noble cause, we must not forget that on a daily basis the majority of harm that befalls people on the internet is due to abuse. It is the understanding and the prevention of this abuse that underlies the need for trust and safety teams throughout tech companies and the topic for the rest of this book.

## What kinds of companies need Trust and Safety functions?

Any company of significance that uses computers for their day-to-day operations needs to have an information security function. But what kind of company needs to think about trust and safety? The obvious first group is companies that allow human beings to interact with one another online. This includes social media companies, messengers, online game platforms, discussion boards, and video platforms. 

Many of these platforms are referred to under the umbrella of “User Generated Content” (UGC) platforms. In any situation where one human can write a message, record a video, or create any other human readable content that is seen by another human there is the likelihood of trust and safety problems. This is true whether the platform is mainly one where content is posted publicly or one where the primary use is for private communications between individuals or small groups.

A second important category is companies that host large amounts of content, such as backup and online storage providers, as well as enterprise cloud computing systems. These kinds of companies can be used to store large amounts of content that either represent or cause harm to individuals, so they will need to have policies and procedures in place to deal with these risks. 

Lately, a broader set of hosting providers and other kinds of infrastructure providers have started to seriously consider trust and safety. The obvious entrants in this space are the cloud providers, from the giants like Amazon Web Services, Google Cloud and Microsoft Azure, to the smaller VPS providers. More specialized infrastructure companies such as Cloudflare and Akamai have also found themselves in difficult situations. These companies are commonly referred to as CDNs or Content Delivery Networks. They run thousands of sites around the world, with computers distributed closer to end users on their home or mobile networks. They also temporarily hold content from their actual customers who pay them to accelerate and protect their sites. These companies are effectively creating entire copies of their customers' platforms and then copying them at least into volatile memory in hundreds of jurisdictions around the world. This is a fundamentally legally and ethically challenging act. And despite some attempts to claim neutrality, these companies have been pulled into the debate of what is acceptable use online.

Payment providers, such as Patreon and Stripe, have found themselves in the crosshairs of activist campaigns due to the fact that they are financially supporting groups who are causing real world harms. And as we will discuss, the explosion of cryptocurrencies have unleashed a whole new way of paying for harmful content and behavior online, bringing in a whole host of new crypto platforms, exchanges, and other firms that need trust and safety functions if they wish to reduce their contributions to harmful activities.

## What do Trust and Safety teams look like?

Trust & Safety teams assemble a swath of functions ranging from content policy, content design and strategy, data science and analytics, engineering, legal, product policy and management, public policy, threat assessment, and research.[^14]

Aside from law enforcement, trust & safety also engages with other external stakeholders such as governments, civil, society, and advertisers. Public policy, communications, and sales & advertiser support take the front lead in this regard, by conducting outreach campaigns and internalizing feedback from these bodies. 

Lastly, all the feedback from the trust & safety teams flows into product design. Product design includes engineers that construct user-facing products. Collaborating with policy, legal, operations, and research teams enables them to ensure that final products meet legal and policy guidelines. 

---
### Key Functions and Roles, from the Trust & Safety Professional Association 

Here, with permission, we reproduce text from the Trust & Safety Professional Association. This content was authored by Harsha Bhatlapenumarthy.  Source: [https://www.tspa.org/curriculum/ts-curriculum/functions-roles/](https://www.tspa.org/curriculum/ts-curriculum/functions-roles/)  

Although not all trust and safety teams are exactly the same, there are key functions and roles that are common across all trust and safety teams. On this page, we profile common functions within trust and safety, with a high-level description of what those teams do and examples of roles within those teams. Smaller companies may have teams that perform multiple functions or team members that play multiple roles. This list is not exhaustive.  

#### Content Policy 
Content Policy is responsible for developing content policies, outlining what type of content is or is not allowed on a platform. These policies usually reflect the company’s values and users’ sensibilities. They also attempt to comply with legal and regulatory requirements, while ensuring that the community’s voice is protected. Where relevant, they may also produce and present internal communications for senior leadership to inform them of ongoing policy situations and provide recommendations and support for decisions. 

Typical Roles: *Content Policy Manager, Policy Analyst, Knowledge Management, Public Policy Manager* 

#### Content Design and Strategy 

Content Design and Strategy identifies the optimal strategy for user-facing content and develops effective language to communicate with users. User-facing content includes user-education material, help center articles, product interventions, etc. 

Typical Roles: *Content Strategist, Content Designer* 

#### Data Science and Analytics 
Data Science and Analytics teams build measurement methods to understand the extent of policy violations present on a platform. They analyze the impact of content moderation, proactive abuse detection, and various other efforts to curb violating content and behavior. They also predict policy violation trends through data analysis, and develop creative ways to address adversarial behavior. 

Typical Roles: *Data Scientist, Data Engineer, Data Analyst* 

#### Engineering 
Engineering is responsible for developing machine learning models to scale and/or automate enforcement against policy-violating behavior. They build and maintain the systems and tools that support user-facing reporting and enforcement options (e.g., DMCA notice-and-takedown), internal review tools,  and other technical aspects of the content moderation and policy enforcement processes. 

Typical Roles: *Software Engineer, Security Engineer* 

#### Legal 
Legal teams are responsible for managing, creating, and articulating responses to requests from law enforcement, regulatory bodies, and government agencies. They proactively identify and mitigate potential issues as well as advise on legal risks. They also counsel product teams and broad cross-functional teams on a wide range of legal issues regarding existing and planned products. 
Typical Roles: *General Counsel, Cybersecurity Law and Investigations, Regional Experts, or Subject Matter Experts (copyright, privacy, etc.)* 

#### Law Enforcement Response and Compliance 

Compliance and Law Enforcement Response teams are responsible for reviewing and accurately assessing legal requests from law enforcement officials, ensuring compliance with applicable law and platform’s terms of service. They respond to sensitive or urgent escalations, process and policy inquiries from law enforcement, government agencies and relevant internal parties. They may also coordinate with internal partners such as Legal and Content Policy and external law enforcement agencies to provide real world assistance to people in crisis. 

Typical Roles: *Law Enforcement Response Analyst, Investigations Analyst, Incident Response Analyst* 

#### Operations 

Operations teams are involved with all aspects of day-to-day moderation activities, and are responsible for developing scalable and efficient processes to support content moderation and policy enforcement. Content moderation professionals are typically housed within operations teams; if a platform chooses to outsource moderation to an external vendor, the platform’s operations team often manages the relationship with that vendor. Other tasks that fall under this group include quality assurance, training, capacity and workflow management, change delivery, developing review protocol, and crisis or incident response and management. Their proximity to content moderation means that operations teams play a key role in generating insights, predicting problem areas, and influencing the future direction of trust and safety work. 

Typical Roles: *Project Manager, Program Manager, Vendor Manager, Analyst, Investigator, Specialist* 

#### Product Policy 

Product Policy teams are responsible for developing and refining principles and policies specific to a particular product (e.g., Ads). Usually a sub-team within Content Policy (which outlines what is or is not allowed on a given platform at a high level), Product Policy teams may introduce additional policy nuances to cater to individual products (e.g., additional restrictions to nudity policies in the context of Ads or Sponsored Content). They also counsel internal product teams and often provide practical product strategies across multiple jurisdictions based on policy considerations. 

Typical Roles: *Product Policy Manager, Product Policy Associate* 

#### Product Management
Product Management partners with engineering, investigators, analysts, operations, policy, and cross-functional leadership to drive the strategy, vision, and execution for preventing and reducing policy violating content and behavior on the platform. “Product,” in this case, may include a policy area such as hate speech or cross-policy focus areas, such as quality assurance or transparency reporting. A product manager for hate speech is responsible for developing the strategy for addressing hate speech on the platform and is accountable for executing the strategy by collaborating with cross-functional teams. 

Typical Role: *Product Manager* 

#### Public Policy and Communications 
Public Policy and Communications is responsible for building and maintaining  partnerships with key external stakeholders such as NGOs, governments, and regulatory bodies. They advise internal teams on regional public policy matters to guide the broader development of products, services, and policies. They manage strategic outreach, designing and leading strategies and campaigns to shape public and political opinion about the platform. 

Typical Role: *Public Policy Manager* 

#### Sales and Advertiser Support 
Although Sales and Advertiser Support is not usually considered a Trust and Safety function, these teams play a key role in addressing advertisers’ concerns about abusive or policy violating content and behavior (e.g., a brand appearing alongside objectionable or extremist content). Typical Roles:*Client Partners, Industry Managers, Vertical Leads* 

#### Threat Discovery and Research 
Threat Discovery and Research teams are responsible for investigating and analyzing networks of abuse, researching bad actor behavior, and streamlining insights to collaborate with both internal teams and relevant external parties, such as law enforcement, to address criminal and/or large scale abuse. 

Typical Roles: *Abuse Investigators, Threat Intelligence Investigators*  

---- 


### How would teams work together on a real Trust and Safety challenge?

Let’s imagine a social media platform called SnickSnack. SnickSnack makes a mobile-first product that is reasonably popular with younger users, but recently has faced headwinds from competitors who have done well with the short, ephemeral video (aka stories) format. SnickSnack’s **head of product** has decided to launch a stories product and puts the product team to work designing and implementing it. 

As an established company with a fully built-out Trust and Safety function, the next steps might go something like this: first, the **product manager** for the new short video product will register the project with an internal tracker. This should trigger reviews by other teams, including **legal**, **privacy** and **product security**. The **product policy team** sees this new product pop up in the timeline and schedules a trust and safety review with the product manager. Along with several experts from the **operations team**, the **product policy manager** then runs a process where known safety risks are considered in the context of this new product. This might even include a formalized threat modeling exercise, although at SnickSnack it takes the form of a more casual brainstorming session.

SnickSnack’s other surfaces have had a problem with child exploitation and trafficking; specifically, their messaging product being used to arrange for the sale of “time” with exploited children. The threat modeling session raises the possibility of the short video format being used to advertise for these kinds of illegal services, as well as the fact that the current enforcement mechanisms and tools are not useful to detect such ads in video.

Coming out of this meeting, several tasks are created to prepare for the launch of this product, with a dedicated **trust and safety product manager** overseeing their implementation. The product policy team determines that their high-level policy against child exploitation is sufficient, but creates new enforcement guidelines and training for the new format. The **safety** **operations team** creates new, dedicated queues for user reports and trains thousands of content reviewers in the new product. The **trust and safety engineering team** implements technical changes to the backend systems in support of these needs and starts work on video content classifiers, although they know that they lack the time and training sets necessary to build something with high recall. Meanwhile, the product team takes feedback from the various trust and safety teams and implements a reporting flow that better reflects the realities of how this product will be consumed by users.

The product launches. As always, the SnickSnack safety teams feel that they aren’t ready, as the **CEO** has pushed this launch to correspond to a key quarterly investor call. The product launches, and the operations team is flooded with abuse reports. Most are useless, but about 5% of the reports around potential child exploitation are deemed to be violative.

During a normal quality assurance process, where a random selection of actioned and non-actioned content is reviewed by a **manager in the content operations team**, the manager overseeing the child safety queue notices a strange pattern of SnickSnacks (as they are now called colloquially) featuring kids dancing in a borderline seductive but not violative way, using the same exact phrases and shot in similar locations. This manager is intrigued by the fact that these videos are being posted regularly by a dozen seemingly unrelated accounts, although they lack the data access or tooling necessary to figure out if these accounts are somehow secretly related. On the hunch that there might be something seriously wrong happening here, the manager creates a ticket in the company’s task management system and sends it to the investigations team.

A **child safety investigator**, who has recently jumped to SnickSnack from an analyst position in the FBI and is still amazed by the breadth and depth of the company’s micro-kitchen, is assigned the ticket by her manager. She opens up the videos spotted by the operations manager and agrees that there is something amiss. She creates a new project in Maltego[^15], and adds the four videos. For each video, she then populates the graph with the IP address, phone number and mobile identifiers for each of the posting accounts. The investigator pretty quickly determines that while these accounts were created using different phone numbers, that each account originated from the same mobile device which was likely used with multiple SIMs. She is also able to see that these accounts conversed with multiple strangers using SnickSnack messenger. 

The investigator documents her suspicions for her manager, who grants her permission to access the account’s private messenger inbox. Upon doing so, she finds that the owner of these multiple accounts would discuss the possibility of meeting the children featured in these videos, using language that strongly hinted at the possibility of sexual contact with the children. In at least one case, the price for such a visit is discussed in detail before the conversation is moved to a competing product known for providing private communications.

The investigator now collects all of this data using the tooling built for her team by the trust and safety engineering function, and includes a writeup of the investigation and supporting evidence in a ticket that she assigns to the company’s **law enforcement response team** (LERT).

An **attorney** **on the LERT team** is assigned this referral due to his previous experience as a prosecutor. He reviews the investigation packet and determines that this reaches the level of a likely case of child sexual exploitation. He then takes two steps: he files a report with the *National Center for Missing and Exploited Children*, as is legally required, and contacts an agent in the FBI office covering the jurisdiction where SnickSnack believes this criminal ring to be operating. The FBI agent takes the description of illegal behavior and works with an Assistant US Attorney to prepare an affidavit and application for a search warrant. Using the SnickSnack investigator’s statement as probable cause, the Federal Magistrate grants the search warrant. The FBI agent sends this warrant back to SnickSnack’s LERT team, which provides the full contents of all conversations involving the suspicious accounts as well as the associated metadata. The LERT attorney notifies the investigator that law enforcement was now appropriately involved, and the investigator disables the violating accounts and all of their content using a process that also preserves the data for future investigations.

As part of their weekly case review, the child safety manager, LERT manager and child safety product manager agree that this case represented a failure of their process. They identify several areas of improvement, including changes to their policy enforcement guidelines to catch the borderline videos earlier in the process and changes to their fake account detector to defeat the exact mechanisms used by this group to create multiple fake accounts. Months later, a member of the **trust and safety research team** publishes an internal slidedeck[^16] summarizing the various child exploitation issues that had been faced by the company, recommending serious changes in the policy enforcement framework as well as the creation of new classifiers so that the company would be less reliant on user reports to catch this pattern of behavior. That feedback is provided to the relevant teams, who add tasks to their long-term roadmaps.

In theory, this is how a well-oiled trust and safety organization should function. In practice, there are many places where this process has fallen apart in the real world, and we will talk about several such situations in this book.

![][image4]

*Figure 4: Trust and Safety Flow.* 

## Trade-offs

Many problems in the trust and safety space are what mathematicians and engineers call “over-constrained”. In the traditional use, an over-constrained problem is one where there are too many requirements for there to be one correct answer. In the field of trust and safety the complications of dealing with human actors, the lack of quantitative measurements of harm, and the fuzziness of many desirable equities makes this problem even harder than finding the right coefficient of friction or designing a bridge. Trust and safety problems almost never present perfectly right answers, only attempts to trade-off various equities that often make none of the proponents of those valid equities happy. 

A classic example of optimization in engineering is the old adage: “You can have this done quickly, cheaply, or correctly. Pick two.” This is called the “Iron Triangle of Engineering” or the “Triple Constraint”, and has been studied extensively by business and engineering scholars[^17]. The idea is that the sponsor of any given project must choose an optimization point between these three goals, and that attempting to get all three can often lead to the customer getting none of the benefits. Government contracting is famous for over-optimizing for low bids in a manner that later leads to cost-overruns or complete failures of projects.[^18]

 ![][image5]	

*Figure 5: Iron triangle of engineering.* 

As part of my years-long war for an eponymous theory or hypothesis, I unveiled the Stamos Dodecagram of Difficult Tradeoffs in my first major talk after leaving industry for Stanford[^19]. The point of this ungainly figure was to demonstrate the many legitimate goals one might have in defining a trust and safety program, and how the tradeoffs between those goals might be surprising and non-linear. 

![][image6]

*Figure 6: Stamos Dodecagram of Difficult Tradeoffs.* 

Here are some key trade-offs platforms wrestle with:

* **Privacy vs Safety** \- For most of the techniques we will discuss in this book to stop online abuses there is the basic assumption that a platform can actually see the abusive behavior. Sometimes, companies might decide to respect privacy by intentionally not looking at data that is available to them, might require a strong investigatory predicate before looking, might lock away data with end-to-end encryption or completely throw it away. There are very good reasons to take all these steps, as we will discuss in detail in our chapter on Surveillance, but most of them also increase the difficulty of detecting, understanding and stopping abuse.

* **Neutrality vs Accuracy** \- Being respectful of freedom of expression[^20] often requires leaving space for irony, comedy, exaggerations and even complete falsehoods, especially when dealing with political speech. Liberal democracies have very complicated legal regimes regarding intentional falsehoods, which often punish targeted falsehoods against private citizens (ie defamation) while allowing political or media actors wide leeway to make false statements of fact even if they are broadly harmful[^21]. Online speech platforms face the same balancing act, which is often made more complex by the reality of at-scale content moderation.

* **Anonymity vs Accountability** \- Online platforms have a wide range of identity policies from requiring a user to prove their identity with government ID to labeling every post on a site as being authored by “Anonymous”. These policies have a significant impact on the incentive structure placed before normal users and the options available to prevent recidivism by users who have been banned for abusive behavior. Anonymous speech has a storied and important history in many countries, including the United States[^22], but in the online world it is also a key enabler of many types of awful abuse.

There is no right answer to these questions, which is one of the reasons why you might want to be skeptical of platforms, academics, journalists or critics who call for absolute adherence to any one laudable goal. 

## Measurement

Without proper measurement, abuse fighting is shooting in the dark.  Measurement should evaluate three things: the size of the badness, the efficiency of badness fighting, and the impact of badness. Badness leads to poor user experience, impacts user trust and in some cases leads to user harm. You should not assume that something bad will be obvious to you, even if you do have reporting. Harm accrues outside of users, so user reporting is not a great input. A strategy is to sample content from the beginning to flag if there are harms you don’t anticipate. 

If you don’t measure harms early on they will get away from you. It is much better to build metrics early when you have more time to react to them. Companies build highly metrasized metrics on the upset and not the downside, prioritizing metrics like MAU (monthly active users), time spent, and interaction rates, and neglecting important harm metrics like prevalence of hate speech. Companies and security teams should prioritize these metrics early on, not only after it is in a newspaper story or in front of Congress. 

![][image7]

*Figure 7: Example distribution of abuses by harm severity, responsibility of product, and users impacted.* 

Facebook used to have a grid that measured impact on the victim (from has a bad product experience to major emotional harm, suicide, death) against how responsible their product is for this bad thing happening. There are bad things that might happen anyway (terrorism) but there are also things that are almost entirely fully facilitated through your product (like sextortion). The level of harm associated with an area of abuse, combined with the prevalence of the abuse, compared with the product’s responsibility for enabling such abuse should determine the prioritization and resources devoted.

Charlotte Willner, the former head of Pinterest’s trust and safety operations team and current director of the Trust and Safety Professional Association, once spoke with us about how trust and safety teams often originate from customer support teams. Some products will have a parallel genesis in security engineering if the product is developed enough to have a security department attached. This often leads to trust and safety operations being run from a customer support lens with customer support focused metrics. The advantage to this is that there is a lot of historical information about how to scale a customer support division and there is more availability of hires from customer service backgrounds. The inherent tradeoff in this positioning is that you are likely not looking at the right metrics for what makes a successful trust and safety operation. Customer support teams focus on metrics like turnaround time and how often users reopen correspondence, as opposed to more tailored metrics like hate speech and harassment prevalence.

### Prioritization

Once you have measurements on what kinds of bad activity happen on a platform, you will need to decide how you want to prioritize your investment in both proactive and reactive trust and safety work. When I joined Yahoo in my first role as CISO, I had a boss named Jay Rossiter. Jay oversaw core infrastructure and services at Yahoo, and at that time had already had a long leadership career in Silicon Valley. One of the many things I learned from Jay was that the core of my job was “portfolio management.” In tackling abuses, it’s easy to say “it’s all important”, but even the largest tech companies have a finite amount of resources[^23]. A critical part of a company security leader’s job is to advocate for growing the resource pie, but in the end there we will always have a limited number of people and financial resources. Those resources should be applied to the issues that both cause the most harm, but also where there will be the best return on the investment a company can make in prevention. 

Effective arguing is one of the most important skills in trust and safety. Safety leaders have to explain complex abuse systems in qualitative terms to engineers and product managers. Quantitative metrics matter a lot for teams, especially engineers and product managers.  If you can measure how someone is impacted by a harm then you can get upper management to put something on their roadmap. Unfortunately, measuring abuse is more complicated than Monthly Active Users and has human impacts that are incredibly difficult to measure. Leaders are often required to influence without authority, working for organizations that are primarily focused on growth. Safety leaders are often trying to convince profit seeking enterprises to justify long term investments in safety, which is not only expensive but brings bad press. Companies are also largely judged by their financial, not their societal harms. Good leadership recognizes user trust is long term central to the success of the company, but not all executive leadership gets it. 

### Proactive versus Reactive

For a long time, trust and safety teams purely created policies and responded to reports. The first proactive work was detection mechanisms to find abusive content before it was reported. Over the last several years, there has been more of a movement to proactively consider how product features can be changed before a product is widely released to prevent abusive behaviors, instead of just planning to react to them. One of the techniques used is red teaming, where trust and safety staff who have experience with a variety of abuse types use products as abusers would to expose hidden vulnerabilities and blind spots. 

There have been a number of high profile incidents that have caused a shift towards more proactive policies. Gamergate and increased awareness of many-on-one harassment (also known as dogpiling) led to thinking more about targeted abuse. Twitter in turn rethought quote tweets and retweets, about how blocking and mentions worked. High-profile murder/suicides on Facebook live have changed how livestreaming platforms redteam and livestream blocking.

Prioritization can also be based upon the amount of amplification provided by various surfaces of a product. A surface is a specific mechanism by which a user might interact with an online system; at Facebook, the same platform had many different surfaces with widely differing amplification and safety aspects. A private message to a single user is clearly different from a safety and privacy perspective than a public post seen by thousands or millions of people, for example. This considerations are often key to deciding what rules, 

![][image8]

*Figure 8: How amplification abilities and right to free expression relate to platform features.* 

## Legal Obligations vs. Awful but Lawful 

The majority of trust and safety decisions made by platforms are done so voluntarily and are not legally mandated, but all such decisions are made within the context of the legal frameworks within which the companies that build and operate these platforms exist. While this is not a legal textbook, having a basic understanding of the legal frameworks around online speech and safety obligations is key to understanding the interplay of forces that drive platform trust and safety regimes.

### American Laws

Most major internet platforms were started in the United States, and some platforms’ early approach to moderation entailed an implicit or explicitly American view of speech, which is that everything that is not specifically disallowed is, by default, allowed. The First Amendment to the U.S. Constitution prohibits government actors from outlawing most of the types of abusive content we discuss in this book because it is constitutionally protected speech. There are key exceptions, and we will cover them (such as CSAM, terrorism, or a credible threat of violence), but the majority of harmful online speech (such as spam, scams, or harassment) is “lawful but awful.” As private actors, the big tech companies are not bound by the First Amendment, and are free to go beyond what is legally required of them in the United States – and generally do, as platforms tend to find that a maximalist approach to speech proves untenable in practice. At the same time, American cultural concerns around free expression have heavily informed their approach.

#### Section 230

Understanding American tech companies’ trust and safety practices requires understanding the federal statute that arguably underpins the modern Internet: 47 U.S.C. § 230, commonly known as “Section 230.” Passed in 1996, Section 230 largely immunizes the provider of an “interactive computer service” (ICS) from civil or criminal liability for its content moderation decisions. The term “interactive computer services” is capacious: it covers websites, blogs, social media platforms, email and messaging services, dating apps, the comments sections of online news articles, and so on.[^24] 

Section 230’s immunity has two main components. First, the law provides that “No provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider” (i.e., another user).[^25] That is, an ICS provider cannot be held liable for what its users say and do. If, for example, a Facebook user posts something defamatory about another person, that user can be sued for defamation, but Facebook cannot. This provision has been called “the twenty-six words that created the Internet,”[^26] because without this protection, services that rely on user-generated content (UGC) may have faced potentially crippling legal exposure as they were just getting started. 

The second way that Section 230 immunizes platforms’ content moderation decisions is by barring liability for “any action voluntarily taken in good faith to restrict access to or availability of material that the provider … considers to be obscene, lewd, lascivious, filthy, excessively violent, harassing, or otherwise objectionable, whether or not such material is constitutionally protected.”[^27] This provision was intended to encourage U.S.-based platforms to moderate “lawful but awful” content, usually as spelled out in their Terms of Service. (Platforms are private companies, not state actors, so their hands are not tied by the First Amendment.) Letting platforms decide what they “consider … objectionable” empowers them to determine their own culture and community norms: for example, an online games site and a dating app might take very different stances on nudity. 

In short, platforms typically cannot be civilly sued or criminally charged in U.S. courts for *leaving up* user speech, nor for *taking down* user speech. Platforms are generally free to moderate – or not moderate – as they choose.

There are a few exceptions. Section 230’s general rule against platform liability for user content does not apply to violations of intellectual property law (such as copyright), federal criminal law (such as the laws against CSAM), or, since 2018, federal sex trafficking law.[^28] For copyright, a different federal statute, the Digital Millennium Copyright Act (DMCA), gives platforms a safe harbor from liability for users’ infringing activities so long as the platform follows certain steps.[^29] (A DMCA-like, court-made rule applies to trademark infringement.[^30]) Yet another federal law gives platforms immunity from liability for user-posted CSAM (which has no First Amendment protection) so long as the platforms remove and report it upon learning of it, though they are not required to look for it.[^31] 

Be aware that these exceptions can get complicated in practice. What’s more, they have been criticized for inducing platforms to “over-remove” non-violative (but perhaps borderline) user content in order to steer far clear of potential liability.[^32] This result flows from the structure of the statutory regime: Section 230 means platforms are not liable for their take-down decisions, but they could be liable for leaving up content that turns out to be CSAM, copyright-infringing, etc. Therefore, risk-averse platforms are incentivized to over-remove content to avoid even the risk of liability.

That said, liability for making a content moderation mistake is exactly what Section 230 aimed to preclude. The law overrode a 1995 New York court decision ruling that Prodigy, an early online service that operated digital bulletin boards, could be held liable as the publisher of an anonymous user’s allegedly defamatory posting.[^33] In holding that the service’s choice to moderate content rendered it potentially liable for any oversights, the *Prodigy* court created what is known as the **“Moderator’s Dilemma”**: “either: (1) moderate content perfectly and accept liability for what’s missed, or (2) not moderate content at all, turning \[services\] into ‘anything-goes’ zones where anti-social content can flourish”[^34] – which would likely drive away users, advertisers, and investors. 

Content moderation is an inevitably imperfect endeavor, though (especially at scale), as any Trust & Safety practitioner knows. Operating a UGC-based service would simply not be feasible had Section 230 not erased the Moderator’s Dilemma. By recognizing this practical limitation and protecting the viability of a then-nascent Internet industry that is now worth trillions of dollars, the 1996 Congress shaped the course of history. 

For most of its existence, Section 230’s statutory immunity was construed broadly by the courts, who usually rejected efforts by the plaintiffs’ bar to plead around Section 230\. In recent years, however, this has come under increasing pressure as the courts have become more amenable to plaintiffs’ arguments – typically in cases with heartbreaking factual allegations of severe real-world harms to users of the defendant services.[^35] 

On top of the courts’ gradual erosion of Section 230’s once-robust protections, the law has seen years of mounting calls in Congress to amend it – or even repeal it entirely, an idea repeated most recently in early 2025.[^36] Why would Congress tinker with its own creation that has enabled so much self-expression, global influence, and economic activity? For one, legislators cannot ignore the impact on their constituents of the online and offline harms that the field of Trust & Safety aims to mitigate. For another, a handful of “Big Tech” companies – few of which existed in 1996 – have amassed alarming amounts of money, power, control over online speech and information flows,[^37] and data about millions of people. But Congress has shown no appetite for antitrust reform and has repeatedly failed to pass comprehensive legislation to protect Americans’ online privacy. That leaves Section 230 as the most obvious other lever. 

Yet by the time of this textbook’s publication, only one bill to amend Section 230 has actually become law: the 2018 carve-out for sex trafficking content.[^38] This is at least partly due to political gridlock: While both parties believe Section 230 should be changed or abolished, they differ as to why, with Democrats worried about harmful content such as hate speech and disinformation and so want platforms to take down *more* content, while Republicans express more concern over platforms’ supposed “censorship” of conservative viewpoints and want platforms to take down *less*.[^39] If Congress does change Section 230, the impetus will likely be child safety, an area of rare bipartisan consensus that has spurred numerous bills over the years to make platforms more accountable for user content.[^40] 

#### Merits Liability and the First Amendment

If Section 230 were to disappear or be materially narrowed, it would revolutionize the field of Trust & Safety. Fearing a flood of expensive lawsuits, platforms would scramble to remove myriad categories of speech, with a bias toward over-removal to be on the safe side. However, lawsuits against platforms over third-party content would not necessarily succeed. The mere removal of statutory immunity does not automatically translate into strict liability. 

As noted, most content online that is considered abusive is nevertheless protected by the extremely broad constitutional right to free speech in the United States. That is, the user who posts such content generally has the right to say it, unless it counts as one of the few unprotected categories of speech (such as CSAM and libel). And platforms, not just their users, have First Amendment rights. As the Supreme Court recently affirmed in the *NetChoice* cases,[^41] the First Amendment protects editorial discretion, and content moderation is just another form of editorial discretion. The Court suggested this applies even when those decisions are executed by algorithm rather than by human moderators. (Of course, that editorial freedom does not extend to hosting unprotected speech such as CSAM nor flouting valid court orders to remove content.) A private platform’s editorial decision not to host awful content – or to leave up content that, while awful, is still lawful speech – is not subject to liability. 

Section 230 thus complements the First Amendment.[^42] The statute promotes judicial efficiency by acting as a procedural express lane for the early dismissal of cases that in many situations would eventually fail anyway, but only after tying up the defendant platform’s (and the court’s) time and resources with lengthy, costly litigation. And the First Amendment is not the only ground on which a case might ultimately fail. In lawsuits against platforms over user content, courts often dismiss the cases on the merits because the plaintiff cannot establish the elements of the claim (such as whether the harm they suffered – for instance a terrorist attack – was actually caused by particular pieces of content). That is, in many cases a platform would not be liable even without Section 230\. 

That was the outcome in a unanimous 2023 Supreme Court decision that held that the family of the victim of an ISIS terror attack would not have been able to sue Twitter for aiding and abetting the terrorists regardless of Section 230\. By hosting ISIS-run accounts, the plaintiffs alleged, Twitter had violated a federal statute against aiding and abetting foreign terrorist organizations. The Court rejected this argument, holding that the plaintiffs failed to show a “concrete nexus” between Twitter’s hosting of the accounts and their injuries – that is, there wasn’t the causal relationship necessary to establish liability.[^43] 

#### The High Cost of Free Speech

It took six years of litigation for the Twitter case to reach its conclusion. That timeline illustrates why, if Section 230 were repealed, platforms – who often have vigorous content moderation practices as-is – would hasten to remove more speech, lawful or not. Litigation in the U.S. is expensive and time-consuming regardless of the outcome. (Unlike in many countries, plaintiffs in American courts don’t generally have to pay the defendant’s costs if the defendant prevails.) 

This is well-understood by the rich and powerful, who would benefit from opening up platform liability for user speech – probably more so than “the little guys,” such as victims of an online dogpiling campaign. Without platform immunity, those with money or power could use (threatened) litigation as a cudgel to get platforms to silence their critics.

Of course, Section 230 has never barred suing users for things they themselves post. But corporate platforms make more attractive targets than, say, the perpetrators of a dogpiling campaign, given companies’ deeper pockets and strategic gatekeeping role over user speech. That said, all platforms are not created equal. The biggest tech companies that enable users to reach the biggest audiences, like Meta or Google, have large legal budgets. However, a tide of lawsuits unleashed by the removal of immunity – or one especially devastating suit – could pose an existential threat to platforms with fewer resources.[^44] 

The biggest tech companies might not mind seeing a competitor eliminated. But having fewer outlets for speaking and receiving information is not a net positive for users (as TikTok’s defenders could tell you[^45]). The shuttering of a UGC service curtails beneficial, innocuous, and harmful speech alike, and with rare exceptions,[^46] the first two categories of content on any service greatly outweigh the last – even if it might not feel like it to those laboring in the service’s Trust & Safety trenches.

### Laws Around the World

If you asked the CEO or General Counsel of every major tech company “Do you follow the law in the places where you do business?” they would answer “Yes, of course.” If you asked the same people “Do you protect the fundamental human rights of your users?” they would also answer “Yes, of course.” Unfortunately, both answers cannot be honest in all circumstances. 

Harms to individuals online do not only come from individuals, but sometimes from sovereign governments with the ability to set and enforce laws. The oldest examples of this problem involve state surveillance. Most of the countries of the world have some kind of legal mechanism to request information from 3rd parties in their own borders. As private (mostly American) companies have become critical in everybody’s lives, many crimes now involve digital evidence, even if the internet was not a key component of the act. For example, robbers using Google Maps to navigate to a bank or reading about fingerprint techniques on wikipedia. Countries around the world have a legitimate need to access evidence of crimes, but sometimes their definition of a crime includes questioning a government ruling in the name of sacred kings or being homosexual. Those are extreme cases, but deciding what laws to respect and which to ignore or fight has become a critical function at tech companies.

More recently, control of the content citizens are allowed to post has become a focus point of both democratic and authoritarian governments. This has been true for a long time, but the breaking point came with NetzDG. For many years, tech companies had responded favorably to legal orders from European courts to take down content or block it from European IPs.

In 2018, the Bundestag passed the German Network Enforcement Act (NetzDG) which requires social media companies to remove “manifestly illegal” speech within 24 hours or face enormous fines. The broad political support for a democratically passed law backed by the legal systems of the entire EU meant that major tech companies had no choice but to proactively enforce German law using their content moderation systems. Since then millions of pieces of content have been flagged by platforms like Facebook and X, with hundreds of thousands deleted.[^47] 

While this has likely led to a decrease in hate speech on the German language sections of major social platforms, it has also encouraged imitators in authoritarian states like Vietnam and Russia. Turkey, the world’s largest jailer of journalists, passed a law mandating social media companies remove content that violates “personal rights” and the “privacy of personal life” within 48 hours or face fines and bandwidth reductions. Turkish lawmakers cited the NetzDG law as inspiration.[^48]

The unsuccessful fight against NetzDG and the benefits the companies saw from turning over a difficult balancing act to lawmakers has significantly changed the tenor of big tech responses to legal requests. There seems to be an assumption of the supremacy of governments that is leading to much more fragmented policies around the world. Companies have to balance what they think is right for their mission and users, with increasing legal restrictions around speech on platforms globally.

Charlotte Willner, the former head of Pinterest’s trust and safety operations team and current director of the Trust and Safety Professional Association, spoke with us about how one of the first things companies need to grapple with is how safety issues and policy implementation will change as the product is scaled globally. Many international growth teams push for entering new markets and getting people to sign up above all else. This can make implementing safety policies that address local challenges difficult. Teams should be thinking about the international implications of their policies early on if they plan to have any international presence. 

## The Rest of This Book

This is an incredibly short introduction to the world of trust and safety. For the rest of this book (and class, if you are taking it) we will dive into some of the specific abuses that bedevil all major and most minor online platforms and cause the most harm online. We will also cover some of the most commonly used techniques to detect and stop these abuses, with the hope that the next generation of entrepreneurs, engineers, product managers, lawyers and other professionals can avoid some of the mistakes of the last.

--- 
[^1]:  https://stanfordio.github.io/TeachingTrustSafety/

[^2]:  [https://explorecourses.stanford.edu/search?view=catalog\&filter-coursestatus-Active=on\&page=0\&catalog=\&academicYear=\&q=cs+152\&collapse=](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&academicYear=&q=cs+152&collapse=) 

[^3]:  This meeting with Mr. Andreessen happened well before his political turn against trust and safety. My recollection is that, while on the board of Facebook, he was supportive of our work to investigate and stop Russian interference in US elections and Facebook’s integrity efforts.

[^4]:  Several tech companies and most media companies have still failed to publicly dissect their failures in 2016, as we will discuss later in this book

[^5]:  This meeting was held in the Aquarium, Mark’s transparent conference room in the middle of the Frank Gehry-designed Building 20 and visible to thousands of visitors each day. The room was packed and the video conference bridge contained around a dozen other employees, including two of my subordinates. When two New York Times reporters called me to comment for a story that included a recounting of this scene, they told me that denying it would be counterproductive as six other employees had already described it to them. 

[^6]:  Those of us who have been in the greater field of “people who hack systems and stop others from hacking them” have preferred the term “information security” since the mid-1990s. The long struggle to avoid the term “cybersecurity”, which was injected into the vernacular by Beltway-types and journalists, has mostly been conceded. 

[^7]:  [https://en.wikipedia.org/wiki/Information\_security\#/media/File:CIAJMK1209-en.svg](https://en.wikipedia.org/wiki/Information_security#/media/File:CIAJMK1209-en.svg) and [https://www.itgovernance.co.uk/iso27000-family](https://www.itgovernance.co.uk/iso27000-family) 

[^8]:  I spent several summers working at LBNL, where Cliff Stoll is a living legend.

[^9]:  Try explaining a dot-matrix printer to a current undergrad if you want to feel old.

[^10]:  If there was to be a traditional academic department for trust and safety it would probably be criminology, which is an area of study not found at many major universities.

[^11]:  The Federal Security Service, or FSB, is one of the three majority intelligence agencies of the Russian Federation and one of the two descended from the KGB. You will hear about them, the SVR and GRU, multiple times in this book as all three have both hacking and information warfare units that I’ve had to deal with.

[^12]:  Measuring ROI in both security and trust and safety is an open issue and the lack of good dependable metrics for either is the source of a great deal of misdirected resources.

[^13]:  In some ways, academic computer science departments are even worse than industry at focusing on the issues that are relevant to real harms. 

[^14]:  https://www.tspa.info/curriculum/ts-curriculum/functions-roles/

[^15]:  Maltego is a popular program among investigators in law enforcement, threat intelligence and corporate investigation teams. It is used to represent the relationship between various objects or individuals involved in an investigation and is often the key tool used for documenting and collaborating on investigations that could include thousands of data points. [https://www.maltego.com](https://www.maltego.com) 

[^16]:  At some companies this slidedeck would then leak, kicking off an unofficial but too-common part of the trust and safety loop, the external scandal.

[^17]:  Pollack J, Helm J, Adler D. What is the iron triangle, and how has it changed? *International Journal of Managing Projects in Business*. 2018;11(2):527-547. https://www.proquest.com/scholarly-journals/what-is-iron-triangle-how-has-changed/docview/2033215603/se-2. 

[^18]:  An exploration of this problem from my home-town newspaper, the Sacramento Bee: https://www.sacbee.com/news/politics-government/the-state-worker/article13595924.html

[^19]:  I was honored to give the 2018 Drell Lecture on “The Battle for the Soul of the Internet”, available here: https://www.youtube.com/watch?v=NKN6xLhTjIo

[^20]:  Throughout this book, we will try to use “Freedom of Expression” to refer to the ideal of both private and public actors allowing for broad expression by individuals, including actions by the private platforms we mostly discuss in this book. “Freedom of Speech” is a phrase that generally invokes freedom from government action and we will endeavor to use it as such. 

[^21]:  See Prof. Cass Sunstein’s review of US law in this area in the Harvard Law Review. https://jolt.law.harvard.edu/assets/articlePDFs/v33/33HarvJLTech387.pdf

[^22]:  The pre-Revolutionary period is a great example of the positive uses of anonymous political speech in the United States. For a detailed discussion of this issue see:  
Kosseff, J. (2022). *The United States of Anonymous: How the first amendment shaped online speech*. Cornell University Press. 

[^23]:  Yahoo, at that point a dying company, had a very finite amount of resources.

[^24]:  The term’s legal definition is “any information service, system, or access software provider that provides or enables computer access by multiple users to a computer server, including specifically a service or system that provides access to the Internet and such systems operated or services offered by libraries or educational institutions.” 47 U.S.C. § 230(f)(2).

[^25]:  47 U.S.C. § 230(c)(1).

[^26]:  Jeff Kosseff, *The Twenty-Six Words that Created the Internet* (Cornell Univ. Press, 2019).

[^27]:  47 U.S.C. § 230(c)(2)(A).

[^28]:  47 U.S.C. § 230(e). 

[^29]:  17 U.S.C. § 512\.

[^30]:  *Tiffany (NJ) Inc. v. eBay Inc.*, 600 F.3d 93 (2d Cir. 2010), *cert. denied*, 562 U.S. 1082 (2010).

[^31]:  18 U.S.C. § 2258A.

[^32]:  Daphne Keller, “Empirical Evidence of Over-Removal by Internet Companies Under Intermediary Liability Laws: An Updated List,” Stanford Ctr. for Internet & Society (Feb. 8, 2021), [https://cyberlaw.stanford.edu/blog/2021/02/empirical-evidence-over-removal-internet-companies-under-intermediary-liability-laws/](https://cyberlaw.stanford.edu/blog/2021/02/empirical-evidence-over-removal-internet-companies-under-intermediary-liability-laws/) (DMCA); Shelby Grossman et al., *The Strengths and Weaknesses of the*

[^33]:  *Stratton Oakmont, Inc. v. Prodigy Services Co.*, 23 Media L. Rep. 1794 (N.Y. Sup. Ct. 1995).

[^34]:  Eric Goldman, “SESTA’s Sponsors Still Don’t Understand Section 230 (As They Are About to Eviscerate It),” Technology & Marketing Law Blog (Mar. 18, 2018), https://blog.ericgoldman.org/archives/2018/03/sestas-sponsors-still-dont-understand-section-230-as-they-are-about-to-eviscerate-it.htm.

[^35]:  See, for example, *Anderson v. TikTok, Inc.*, where a federal appeals court controversially ruled that Section 230 did not bar a lawsuit brought by the mother of a ten-year-old girl who asphyxiated to death after engaging in a “blackout challenge” she allegedly saw on TikTok. 116 F.4th 180 (3d Cir. 2024).

[^36]:  U.S. Senate Committee on the Judiciary, “Durbin Delivers Opening Statement During Senate Judiciary Committee Hearing On Stopping The Exploitation Of Children Online” (Feb. 19, 2025), https://www.judiciary.senate.gov/press/dem/releases/durbin-delivers-opening-statement-during-senate-judiciary-committee-hearing-on-stopping-the-exploitation-of-children-online; U.S. Senate Committee on the Judiciary, “Ending the Scourge: The Need for the STOP CSAM Act” (Mar. 11, 2025), https://www.judiciary.senate.gov/committee-activity/hearings/ending-the-scourge-the-need-for-the-stop-csam-act.

[^37]:  Daphne Keller, *Who Do You Sue?: State and Platform Hybrid Power over Online Speech*, Hoover Institution Aegis Series Paper No. 1902 (2019), https://www.hoover.org/research/who-do-you-sue.

[^38]:  Tom Jackman, “Trump signs ‘FOSTA’ bill targeting online sex trafficking, enables states and victims to pursue websites,” The Washington Post (Apr. 11, 2018), https://www.washingtonpost.com/news/true-crime/wp/2018/04/11/trump-signs-fosta-bill-targeting-online-sex-trafficking-enables-states-and-victims-to-pursue-websites/.

[^39]:  Marguerite Reardon, “Democrats and Republicans agree that Section 230 is flawed,” CNET (June 21, 2020), https://www.cnet.com/news/politics/democrats-and-republicans-agree-that-section-230-is-flawed/.

[^40]:  *See* “Durbin Delivers Opening Statement,” *supra* note TKTK.

[^41]:  *See* Krista Chavez, “NetChoice Wins at Supreme Court Over Texas and Florida’s Unconstitutional Speech Control Schemes,” NetChoice (July 1, 2024), https://netchoice.org/netchoice-wins-at-supreme-court-over-texas-and-floridas-unconstitutional-speech-control-schemes/. 

[^42]:  *See generally* Eric Goldman, *Why Section 230 Is Better Than the First Amendment*, 95 Notre Dame L. Rev. Reflection 33 (2019).

[^43]:  *Twitter, Inc. v. Taamneh*, 598 U.S. 471 (2023).

[^44]:  Digital media company Gawker Media experienced this firsthand: it was forced into bankruptcy by a massive monetary verdict in a Peter Thiel-financed lawsuit brought by celebrity wrestler Hulk Hogan for publishing an excerpt of a sex tape online. Bill Chappell, “Gawker Files For Bankruptcy As It Faces $140 Million Court Penalty,” NPR (June 10, 2016), [https://www.npr.org/sections/thetwo-way/2016/06/10/481565188/gawker-files-for-bankruptcy-it-faces-140-million-court-penalty](https://www.npr.org/sections/thetwo-way/2016/06/10/481565188/gawker-files-for-bankruptcy-it-faces-140-million-court-penalty). Gawker’s First Amendment arguments failed, and Section 230 had no applicability, as Gawker was being sued for its own speech, not a user’s.

[^45]:  *E.g.*, Jacob Mchangama and Jeff Kosseff, “Banning TikTok Would Violate America’s Free Speech Tradition,” Wall St. J. (Jan. 2, 2025), https://www.wsj.com/politics/policy/banning-tiktok-would-violate-americas-free-speech-tradition-a27bd88a.

[^46]:  *See* Eduardo Medina, “Omegle Shuts Down as Founder Acknowledges Crime on Video Chat Site,” N.Y. Times (Nov. 9, 2023), https://www.nytimes.com/2023/11/09/business/omegle-shuts-down.html.

[^47]:  https://futurefreespeech.com/the-digital-berlin-wall-how-germany-accidentally-created-a-prototype-for-global-online-censorship-act-two/

[^48]:  https://www.eff.org/deeplinks/2020/07/turkeys-new-internet-law-worst-version-germanys-netzdg-yet

[image1]: images/figure1.png

[image2]: images/figure2.png

[image3]: images/figure3.png

[image4]: images/figure4.jpg

[image5]: images/figure5.png

[image6]: images/figure6.png

[image7]: images/figure7.png

[image8]: images/figure8.png
