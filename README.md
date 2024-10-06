# Nasaspaceapps-code
Problem: After monitoring and recording seismic behaviour on other planets, the recorded data has to be sent back to earth. However the data is usually extremely large and mostly composed off background noises.

Aim: detect earthquakes within seismic data

solution criteria:
- Has to not be computationally expensive
- Run fast
- Not exclude any earthquakes
- False positives should be kept to a minimum preferably non-existent


Solution: 
- Get maximum points of the graph
- if they region around this point has a large average value it is likely to be a earthquake
- this satisifies most of the criteria
- rarely returns false positives 
