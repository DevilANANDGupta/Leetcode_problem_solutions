class Solution {
   int[][] grid;
  
   public int maxAreaOfIsland(int[][] grid) {
      this.grid = grid;
      // in case of it's empty matrix we will return 0
      if (grid.length == 0)
         return 0;
     
      int ans = 0;
      //traversal of all the elements in the grid
      for (int r = 0; r < grid.length; r++) {
         for (int c = 0; c < grid[0].length; c++) {
            ans = Math.max(ans, area(r, c));
         }
      }
      return ans;
   }

   public int area(int r, int c) {
      // condition to skipping all invalid and processed blocks from matrix
      if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == 0)
         return 0;
      // unset the bit
      grid[r][c] = 0;
     // recursively traversing till depth of Island with increament
      return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1);
   }
}
