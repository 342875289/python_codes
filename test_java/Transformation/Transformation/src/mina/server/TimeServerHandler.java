package mina.server;
import java.util.Date;

import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IdleStatus;
import org.apache.mina.core.session.IoSession;
 
 
public class TimeServerHandler extends IoHandlerAdapter {
 
    //�����쳣
    @Override
    public void exceptionCaught( IoSession session, Throwable cause ) throws Exception
    {
        cause.printStackTrace();
    }
    //��Ϣ����
    @Override
    public void messageReceived( IoSession session, Object message ) throws Exception
    {
        String str = message.toString();
        if( str.trim().equalsIgnoreCase("quit") ) {
            session.close();
            return;
        }
        System.out.println("my message>>>>>>>>>>"+str);
        Date date = new Date();
        if("hello6".equals(str)){
        	session.write("close");
        }else{
        	session.write( date.toString() );
        }
    }
    //�Ự����
    @Override
    public void sessionIdle( IoSession session, IdleStatus status ) throws Exception
    {
        System.out.println( "IDLE " + session.getIdleCount( status ));
    }
}
