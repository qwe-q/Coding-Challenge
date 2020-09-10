Enclosed in the main.py file is my solution to the ACM Research Coding Challenge #1. 
This solution is implemented using the DBSCAN algorithm, an algorithm for grouping clusters of elements
that is based on the density of related elements. This algorithm seemed the best fit for the prompt of "determin[ing]
the number of clusters" as the challenge presented.

This code should not be taken as a measure of my experience with CS algorithms... It isn't. What this is is a testament
to my ability to problem solve and learn new ideas and methods. Without any prior knowledge on the subject of clustering,
I managed to understand and implement DBSCAN in two days. I had a blast putting it all together!

The Epsilon and MinPoints values that the DBSCAN algorithm requires are declared as global variables at the top of the
program. (This code isn't exactly the cleanest in the world.) I played around with these values a bit until I got a
result I liked- my implementation and values are able to detect four main clusters, with one outlier in the middle, and the noise at
the edges also being detected as a new cluster. You, the reviewer, are invited to play around with these values for
yourself, and see what results the algorithm can bring you with different inputs.

This code uses matplotlib to render the graph. Each cluster is rendered as a new color, which ends up looking quite
nice. The default backend is used. 

Also, it turned out that my solution was exactly 100 lines long. I had a laugh when I saw that!