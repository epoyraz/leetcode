import java.util.concurrent.Semaphore;
import java.util.concurrent.CyclicBarrier;

class H2O {
    private Semaphore hydrogenSem = new Semaphore(2);
    private Semaphore oxygenSem = new Semaphore(1);
    private CyclicBarrier barrier = new CyclicBarrier(3);

    public H2O() {}

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        hydrogenSem.acquire();
        try {
            barrier.await(); // Wait until 3 threads reach (2H + 1O)
            releaseHydrogen.run();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            hydrogenSem.release();
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        oxygenSem.acquire();
        try {
            barrier.await();
            releaseOxygen.run();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            oxygenSem.release();
        }
    }
}
