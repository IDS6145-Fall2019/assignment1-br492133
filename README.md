
# Assignment 1 - Designing Models and Analyzing Data 

> * Participant name: Bradley 'Austin' Kriznar
> * Project Title: SUBWAY MODEL ANALYSIS

# General Introduction

The first part of this assignment explores designing models (and basic Python/Git features). 

We will look at **subway model in a city** system. A **subway system** is an underground, tube, or metro, underground railway system used to transport large numbers of passengers within urban and suburban areas - modern subways use different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently. 

The second part of the assignment explores data analysis. Data analysis and visualization is key to both the input and output of simulations. This assignment explores different random number generators, distributions, visualizations, and statistics. Additionally, it will look at getting you accustomed to specifying input and output variables to a system. We will also practice working with real data.


# Part 1: Designing a Model - Subway System
Subway transportation is incredibly important for many metroplitian areas. It is magnitudes of order more effective for traffic mitigation than individuals using cars in their commutes, and so making sure existing subways queue / run efficiently is certianly a worthy priority for city planners.   

There are a large number of examples of these kinds of queues. In London, the Underground logs up to 5 million journeys a day. The majority of passengers must enter the Underground via escalator tunnels, especially in the dowtown area. Ensuring appropriete passenger safety entering and exiting the subway is important for smooth operation, balanced with speed (it would make no sense to have escalators when they are slower than just taking the stairs).


![Image of Subway City System](images/subway_model.png)

## (Part 1.1): Requirements (Experimental Design) **(10%)**

* The system **shall [01]** model subway entrance and exit escalators.
* The system **shall [02]** model an escalator compliant with ASME A17.1-2007/CSA B44-07, Safety Code for Elevators and Escalators, Part 6 Escalators and Moving Walks. 
* The system **shall [03]** have step deck of length between 22 in. and 40 in.
* The system **shall [04]** have step run of no less than 15.75 in. 
* The system **shall [05]** have step rise of no more than 8.5 in.  
* The system **shall [06]** model escalator incline at an angle of no greater than 30 degrees.
* The system **shall [07]** model belt speed not exceeding 100 ft / min. 
* The system **shall [08]** model assume a constant belt speed.
* The system **shall [09]** model people riding an escalator.
* The system **shall [10]** assume no more than one person per escalator step.
* The system **shall [11]** assume people do not change escalator steps once on the escalator.
* They system **shall [13]** process input data of the file format Comma Separated Values
* The system **shall [14]** analyze the model and be capable of outputting said analysis.
* The system **shall [15]** analyze the model through use of descriptive statistics.
* The system **shall [16]** utilize programming language Python for to model.
* An object diagram **shall [17]** be used to describe the system.
* A class diagram **shall [18]** be used to describe the system.
* A state transition diagram **shall [19]** be used to describe the system.
* An agent / user case diagram **shall [20]** be used to describe the system.


## (Part 1.2) Subway (My Problem) Model **(10%)**

* [**Object Diagram**](images/Subway_Object_Diagram.png) - provides the high level overview of subway model objects.
* [**Class Diagram**](images/Subway_Class_Diagram.png) - provides simple class detail for objects in the model.
* [**Behavior Diagram**](images/Behavior_Activity_Diagram.png) - provides details of a simple subway escalator use case.
* [**Agent / User case** (if appropriate)](images/Agent_Case_Diagram.png) - provides details of a simple subway escalator use case.

## (Part 1.3) Subway (My Problem) Simulation **(10%)**

Ideally, I would use a dedicated tool to utilize for this simulation such as **Simio.** The escalator can be largely treated as a queue - people are assumed not to 'move' up or down on the escalator steps (relative to the escalator steps, they are not moving) and are 'processed' by the server at a fixed rate with a fixed speed. The stochastic flow of people into the server (escalator) would be based on sampled data (hourly, daily, weekly) collected from real turnstile or open sources. This is where the interesting part of the simulation - is the escalator too crowded? Is there a line to get onto the escalator? If so, how long is the line? How long are people waiting, on average, to actually utilize the escalator? I would base my experiment with those questions in mind. It could be represented as a mixed kind of discrete and agent-based simulation.

Doing a little research, American Society of Mechanical Engineers (ASME) standards govern the maximum escalator speed at 100 ft / min; anecdotally this seems like a fair representation to what I have personally experienced as an escalator's normal operating speed and should work as a simulated assumption. Additionally, assuming the ASME designation for step length of 8.5 in. and one person per step, the escalator can be treated roughly as the hypotenuse of an imaginary triangle (bound between the elevation gap (the rise) and the ground (the run)). That hypotenuse length dictates the server capacity in the model (hypotenuse length / 8.5 in. = approximate step number). Modeled as a queue, the 'escalator' has a server capacity equal to maximum step number; escalator users (agents) are 'processed' at a constant rate (process time = escalator speed / step number) and may enter the queue as the escalator stairs are made available **(at a constant rate )**. Escalators do not change size (the hypotenuse is fixed) and thus the queue capacity and time on escalator are constant. 

In context of Python, individual steps can have associated indices in the that have the associated state of occupied or unoccupied. Agents on the objects temporarily lock the step index until the have spent enough time being processed. Once the correct amount of time has passed, the rider leaves the step and the index is freed again to be used. One import constraint that would have to be considered with simulating the escalator this way is that only one index may be made available for agents at a time (i.e. if only four people are one an escalator with 100 steps, can 96 people instantly get on a step?).  


## (Part 1.4) Subway City (My Problem) Model **(10%)**
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)
You are expected to create the python files - the code should run without errors, create and object(s) for your system, but not provide function detail.

[**Basic Subway Model**](code/Subway_Model_2)



## (Part 1.5) Specifying the Inputs to a System **(10%)**
**Specify the independent and dependent input variables of your subway escalator model**

Independent Variables – 

* The **escalator step dimensions** are fixed and required to be a fixed size.
* The **escalator belt speed** is assumed to be fixed. The number of people on the escalator does not have an effect on its speed as the real system is highly standardized. 
* The **maximum step capacity** is assumed to be independent as we do not believe the escalator will change length, as with real life.

Dependent Variables -

* The **person arrival rate, lambda** is dependent on the time of day. This is based on the idea subways are likely used more at different times – we may expect that ridership (and thus escalator usage) is tied to when people are coming and going to work.
* The **person size** is dependent on a few factors, including if they are a child (likely to be smaller and take only a single escalator step) or an adult (likely to be larger and may take a few steps up).
* The **escalator queue entrance availability** is dependent on the number of people currently on the escalator. If the escalator is at a full steady-state, then a line will begin to form to get onto the escalator (assuming people are standing single-abreast). 

**Specify where the data will come from measured subset of real data (empirical) or synthetic data**

Ideally, direct sampling to collect real data would be done use as the base of the simulation data. That is not really likely. Luckily, a few quick searches on Google provide large set of real turnstile / usage data directly from the Metropolitan Transportation Authority (MTA) (here at: http://web.mta.info/developers/download.html). While turnstile data does not directly map onto escalator use in subways, it could be a great starting point. 

**What kind of statistics are important to capture this input data**

I think it would be important to capture basic descriptive statistics for arrival rates, escalator belt speed / size, and usage information as related to time of day / day of week.  

**How do you plan to analyze the output of your model**

It would be useful to determine and analyze what the queue length waiting to enter the escalator is on average (average wait time). That is probably the most productive question to get an answer for, especially if in a very-high traffic station such as Times Square or Grand Central Terminal. 

**What ways will you visualize your data - charts, and graphs you will create**

A bar graph depicting average escalator wait time across a day, with each day represented as a separate line, could be a clear way to visualize traffic variability. It may also be interesting to see usage or non-usage data that is subway station dependent (are there escalators that cost more to operate in maintenance costs and electricity than is covered by the local ridership fare?). 

**What clever way will you visualize your output with a useful infographic?**

I think it would be helpful (if speaking to government officials or city planners about escalator usage) to make an infographic that concisely compares the relative usage percentage of escalators and what impacts (number of steps saved, time saved, etc.) for riders that additional escalators may provide. Also, if there are stations where the escalators are already potentially overloaded and less effective than taking the stairs. It could aesthetically look a bit like an up escalator with factoids that are showing growth going up and the converse for potential time saved, etc. going down. 


# Part 2: Creating a Model from Code

## (Part 2.1) **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model **(10%)**
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template for the code found in  [**the following folder**](code/POTS_system/). Please create a **class** diagram of this model.

[**POTS Model Class Diagram**](images/POTS_Class_Diagram.png)

# Part 3: Data Analysis

## (Part 3.1) - Real Data **(10%)**

Find a datasource that looks at part of this model - subway stations locations / escalator number, heights, widths / volume of passangers - ridership numbers   (*fits* - we are pretty loose here, it can be anything.)

**Write up a paragraph that describes the data and how it fits into your system.**

There is not really a lot of non-engineering information (see above about ASME standards) that directly applies to escalators, especially in respect to usage, available online. I think that it could be useful as a proxy to learn more about general subway ridership. Station ridership data gives a partial context of escalator use. To be clear, not everyone who enters or exits a subway uses escalators – options such as stairs minimize cost to maintain; elevators are ADA compliant and support wheelchair users. The ridership data is useful in the ideal model of the escalator as a way to roughly gauge queue lengths, especially if information about a particular station is known (number of entrances and exits, number of stairways, escalators, and elevators, etc.). This ridership data could be used to focus on which stations could see the greatest benefit from more extensive sensitivity analysis. Stations such as Grand Terminal Station and Madison Square Garden hare grouped into the ‘Top 10’ riders; these stations handle millions of trips per week. They represent ideal places to model comprehensively through the use of actual time sampling and data collection on-site.

**Load the data into Python**

[**MTA_Station_Ridership_Data**](code/MTA_Stations_Data1.csv)

**Calculate a few useful statistic on the data - keep it simple- STD, means, etc..., this is just designed * to get used to working with real data. Explain the insights you derive from these statistics.**

Of the 100 New York MTA stations analyzed, approximately the top 30 by average weekly ridership made up over half the total rides. This suggests that most-likely to be used escalator models can be condensed to nearly 30 of interest to understand more than half of all MTA trips in New York. One interesting trend among the standard deviations is that the Weekend ridership variation is relatively quite high. This makes sense – tourism and events are more likely on the weekend and stable variation is expected during the week from routine commuters.  

[**3_1 Code with statistics output**](code/3_1.py)

**Visualize the raw data - visualize a few critical aspects of the data to better describe what it is, what it is showing, and why its useful to your system.**
**Calculate and plot some summary statistics that better describe the data.**

![Test](images/Figure_3_1_1.png)
![Test](images/Figure_3_1_2.png)



## (Part 3.2) -  Plotting 2D Random Number Generators **(15%)**

This portion of the assignment looks at generating random numbers in Python and understanding how to properly plot them. Plot two different random numbers, pseudo random and quasi random, for five different N values. There should be 10 subplots, all properly formatted 2D plots. Note, each of the N points will have two coordinates, an x and a y, therefore you will need to generate two random numbers for each point. You should replace the image with your results in a simalar format. Discuss how the patterns differ. Feel free to change the N values from the suggested N values in the image to state your case.

[**3_2 Code**](code/Test3_2.py)

The pseudo-random numbers are plotted with N-many points with respective x,y values generated with a random values and shifting seed values. The quasi-random points are created using the Sobol sequence of array length-N. The x-values are the linear Sobol sequence; the y-values are the same sequence offset by an index of 99. 

The comparison of the two could not be more distinct – the pseudo-random points are ‘evenly’ distributed and appear to cluster and become denser radially as the number of points increase (the mean being 0 and standard deviation being 1); the quasi-random points exhibit extreme order and patterns. This makes sense as the Sobol values have a set sequence order - we would expect emergent patterns to be quite stark. The pseudo-random numbers don't exhibit order outside of the density observed toward the mean (this is expected).

![Test](images/Figure_3_2a.png)


## (Part 3.3) -  Plotting 1D Random Distributions **(15%)**

Now, choose three different distributions to plot in 1D, or as a histogram. Choose a pseudo-random generator and generate three different distributions. Example distributions are Uniform (part 8), Normal, Exponential, Poisson, and Chi-Squared, but feel free to use any three distributions of your choice. Again, plot each distribution for five different Ns. This will result in 15 different subplots, formatted similar to the image in Part 8. **Include your properly formmated 1D plots below and breifly describe what we are looking at and how things change as N is changed.**

[**3_3 Code**](code/3_3_Quasi_Bar_Charts.py)

![Test](images/Figure_3_3a.png)

The standard normal and exponential histograms look relatively normal about the mean (this should be expected). With a number of bins equal to 35, the two distributions take noticeable shape between N=100 and N=500. Both begin to form ‘smooth’ curves as N increased. Conversely, the uniform distribution is all over the place. It spans the width of the area with no discernable ‘curve’; we expect this because values should be **uniformly** distributed. No significant clustering can be detected with visual inspection and 35 bins; if bin size and N where both increased then some clustering may be detected.

**Repeat the above using a quasi-random generator. Discuss the similarities and differences.** 

[**3_3 2_Code**](code/3_3_Bar_Charts.py)

![Test](images/Figure_3_3_2.png)

The quasi-random distribution used the Sobol sequence and is most similar to the uniform distribution above but contains far less variation among the frequencies of the values (represented by peak height). The N=5000 histogram is virtually a square, which the respective uniform does not look nearly as representative of. The visual difference between N=100 and N=500 for the Sobol sequence and uniform distribution show this difference well.
