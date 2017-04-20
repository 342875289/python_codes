package com.test.http;

import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IdleStatus;
import org.apache.mina.core.session.IoSession;

public class ServerHandler extends IoHandlerAdapter {
    public void sessionOpened(IoSession session) {
        // set idle time to 60 seconds
//        session.setIdleTime(IdleStatus.BOTH_IDLE, 60);
    }

    public void messageReceived(IoSession session, Object message) {
        // Check that we can service the request context
        HttpResponseMessage response = new HttpResponseMessage();
        //response.setContentType("text/plain");
        response.setResponseCode(HttpResponseMessage.HTTP_STATUS_SUCCESS);
        response.appendBody("¡¨…œ¡À");

        // msg.setResponseCode(HttpResponseMessage.HTTP_STATUS_SUCCESS);
        // byte[] b = new byte[ta.buffer.limit()];
        // ((ByteBuffer)ta.buffer.rewind()).get(b);
        // msg.appendBody(b);
        // System.out.println("####################");
        // System.out.println("  GET_TILE RESPONSE SENT - ATTACHMENT GOOD DIAMOND.SI="+d.si+
        // ", "+new java.text.SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss.SSS").format(new java.util.Date()));
        // System.out.println("#################### - status="+ta.state+", index="+message.getIndex());

        //// Unknown request
        // response = new HttpResponseMessage();
        // response.setResponseCode(HttpResponseMessage.HTTP_STATUS_NOT_FOUND);
        // response.appendBody(String.format(
        // "<html><body><h1>UNKNOWN REQUEST %d</h1></body></html>",
        // HttpResponseMessage.HTTP_STATUS_NOT_FOUND));

        if (response != null)
            session.write(response).isWritten();
    	Thread taskThread = new Thread(new Runnable() {
			@Override
			public void run() {
		        int i=0;
		        while(session.isConnected()){
		        	//response.appendBody(++i+"");
		        	session.write(i++);
		        	try {
						Thread.sleep(1000);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
		        }
			}

			
		});

		
		taskThread.start();

    }
  
    public void sessionIdle(IoSession session, IdleStatus status) {
        session.close();
    }

    public void exceptionCaught(IoSession session, Throwable cause) {
        session.close();
    }
}
