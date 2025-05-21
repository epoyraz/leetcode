import java.util.concurrent.CountDownLatch;

public class Foo {
    private CountDownLatch latch1;
    private CountDownLatch latch2;

    public Foo() {
        latch1 = new CountDownLatch(1);
        latch2 = new CountDownLatch(1);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run(); // prints "first"
        latch1.countDown(); // allow second() to run
    }

    public void second(Runnable printSecond) throws InterruptedException {
        latch1.await(); // wait until first() completes
        printSecond.run(); // prints "second"
        latch2.countDown(); // allow third() to run
    }

    public void third(Runnable printThird) throws InterruptedException {
        latch2.await(); // wait until second() completes
        printThird.run(); // prints "third"
    }
}
