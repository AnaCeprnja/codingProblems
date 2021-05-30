/*The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.


sleepIn(false, false) → true
sleepIn(true, false) → false
sleepIn(false, true) → true */
public boolean sleepIn(boolean weekday, boolean vacation) {
  if (!weekday || vacation) {
    return true;
  }
  
  return false;
  
  // Solution notes: better to write "vacation" than "vacation == true"
  // though they mean exactly the same thing.
  // Likewise "!weekday" is better than "weekday == false".
  // This all can be shortened to: return (!weekday || vacation);
  // Here we just put the return-false last, or could use an if/else.
}

/*Given an array of ints, return true if 6 appears as either the first or last element in the array. The array will be length 1 or more.


firstLast6([1, 2, 6]) → true
firstLast6([6, 1, 2, 3]) → true
firstLast6([13, 6, 1, 2, 3]) → false */
public boolean firstLast6(int[] nums)
{	return (nums[0] == 6 || nums[nums.length-1] == 6);	}

// Given an array of ints, return true if the array is length 1 or more, and the 
// first element and the last element are the same. 
public boolean sameFirstLast(int[] nums)
{	return (nums.length >= 1 && nums[0] ==  nums[nums.length-1]);}







//print something that returns hello and a name