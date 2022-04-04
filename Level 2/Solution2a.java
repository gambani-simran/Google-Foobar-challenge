//Ion Flux Relabeling

import java.util.Arrays; 

public class Solution2a {
    
    Node root; 

    static class Node { 
        int data; 
        Node left, right; 
        Node(int data) 
        { 
            this.data = data; 
            this.left = null; 
            this.right = null; 
        } 
    } 
    
    public Node buildPerfectBinaryTreeUtil(int[] arr, Node root, int i) 
    { 

        if (i < arr.length && arr.length != 0) { 
            Node temp = new Node(arr[i]); 
            root = temp; 

            // insert left child
            int[] arrl = Arrays.copyOfRange(arr, 0, i/2);
            root.left = buildPerfectBinaryTreeUtil(arrl, root.left, 
                                            (i/2 - 1)); 

            // insert right child 
            int[] arrr = Arrays.copyOfRange(arr, i/2, i);
            root.right = buildPerfectBinaryTreeUtil(arrr, root.right, 
                                            (arrr.length-1)); 
        } 
        return root; 
    }
    
    static int findParent(Node node, int val, int parent) 
    { 
        int pl = 0;
        int pr = 0;
        if (node == null) {
            return parent; 
        }

        if(node.data == val) {
            return parent;
        }

        if (node.left != null) {
            if (node.left.data == val)
                return node.data;
            pl = findParent(node.left, val, node.data);
        }

        if (pl == 0) {
            if (node.right != null) {
                if (node.right.data == val)
                    return node.data;
                pr = findParent(node.right, val, node.data);
            }
        } else {
            return pl;
        }
        return pr;
    }
    
    public static int[] solution(int h, int[] q) {
        // Your code here
        int numOfNodes = (int)Math.pow(2, h) - 1;
        int arr[] = new int[numOfNodes];
        for (int i = 0; i < numOfNodes; i++) {
            arr[i] = i+1;
        }

        Solution t2 = new Solution();

        t2.root = t2.buildPerfectBinaryTreeUtil(arr, t2.root, arr.length-1); 

        int[] result = new int[q.length];
        int p;
        for (int j = 0; j<q.length; j++) {
            p = findParent(t2.root, q[j], -1);
            result[j] = p;
        }

        return result;
    }
}