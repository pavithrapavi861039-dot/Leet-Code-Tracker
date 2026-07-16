// Last updated: 7/16/2026, 4:11:44 PM
import java.util.*;
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorder(root, result);
        return result;
    }
    private void inorder(TreeNode node, List<Integer> result) {
        if (node == null) return;

        inorder(node.left, result);   
        result.add(node.val);         
        inorder(node.right, result);  
    }
}