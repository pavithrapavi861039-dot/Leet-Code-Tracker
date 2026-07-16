// Last updated: 7/16/2026, 4:08:16 PM
import java.util.*;
class MyStack {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();
    public void push(int x) {
        q1.add(x);
    }
    public int pop() {
        while (q1.size() > 1) {
            q2.add(q1.remove());
        }
        int top = q1.remove();
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
        return top;
    }
    public int top() {
        while (q1.size() > 1) {
            q2.add(q1.remove());
        }
        int top = q1.peek();
        q2.add(q1.remove());
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
        return top;
    }
    public boolean empty() {
        return q1.isEmpty();
    }
    public static void main(String[] args) {
        MyStack s = new MyStack();
        s.push(1);
        s.push(2);
        System.out.println(s.top());  
        System.out.println(s.pop());   
        System.out.println(s.empty()); 
    }
}