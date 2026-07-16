// Last updated: 7/16/2026, 4:07:40 PM
import java.util.*;
public class Codec {
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        helperSerialize(root, sb);
        return sb.toString();
    }
    private void helperSerialize(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("null,");
            return;
        }
        sb.append(node.val).append(",");
        helperSerialize(node.left, sb);
        helperSerialize(node.right, sb);
    }
    public TreeNode deserialize(String data) {
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));
        return helperDeserialize(queue);
    }
    private TreeNode helperDeserialize(Queue<String> queue) {
        String val = queue.poll();
        if (val.equals("null")) return null;
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = helperDeserialize(queue);
        node.right = helperDeserialize(queue);
        return node;
    }
}