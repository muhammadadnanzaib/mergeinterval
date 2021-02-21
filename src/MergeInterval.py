class MergeInterval:
  def __init__(self, interval_list):
    """Assuming the interval list is composed of list (must be mutable) pair of interval, 
    where first entry is less than second"""
    self._interval_list = interval_list[:] # Making a copy for internal usage
    self._output_list = [] # Default empty output list

  def __sort(self):
    """ Sorts interval list based on first value of each pair in list"""
    # https://stackoverflow.com/questions/8459231/sort-tuples-based-on-second-parameter
    self._interval_list = sorted(self._interval_list, key = lambda x: x[0])
    return self._interval_list
  
  def __merge_interval(self, interval):
    smaller_interval = self._output_list[-1] # last entry in our output list is largest interval which can be merged, if possible
    larger_interval = interval
    
    if larger_interval[0] > smaller_interval[1]: # no overlap condition   
      self._output_list.append(larger_interval)
    else:
      self._output_list[-1][1] = max(smaller_interval[1], larger_interval[1])
    return 

  def merge(self):

	if self._interval_list: # check if list is non-emtpy
      self.__sort() # sort interval list containing based on first entry of all intervals
      self._output_list.append(self._interval_list.pop(0))  
      # Merge two interval and do it for all elements in interval list
      for interval in self._interval_list:
        self.__merge_interval(interval)

    return self._output_list


if __name__ == "__main__":
	to_merge = [[25,30], [2,19], [14, 23], [4,8] ]
	mi = MergeInterval(to_merge)
	result = mi.merge()

	print(to_merge)
	print(result)	