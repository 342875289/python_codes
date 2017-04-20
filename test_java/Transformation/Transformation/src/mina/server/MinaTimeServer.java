package mina.server;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.charset.Charset;
 
import org.apache.mina.core.service.IoAcceptor;
import org.apache.mina.core.session.IdleStatus;
import org.apache.mina.filter.codec.ProtocolCodecFilter;
import org.apache.mina.filter.codec.textline.TextLineCodecFactory;
import org.apache.mina.filter.executor.ExecutorFilter;
import org.apache.mina.filter.logging.LoggingFilter;
import org.apache.mina.transport.socket.nio.NioSocketAcceptor;
 
public class MinaTimeServer {
    private static final int PORT = 9125;
    public static void main(String[] args) {
        //socket������
        IoAcceptor acceptor = new NioSocketAcceptor();
 
        //�����־��¼
        acceptor.getFilterChain().addLast("logger", new LoggingFilter());
        //��ӱ�������� 
        acceptor.getFilterChain().addLast("codec",new ProtocolCodecFilter(new TextLineCodecFactory(Charset.forName("UTF-8"))));
       // acceptor.getFilterChain().addLast("threadPool", new ExecutorFilter());  
        //��Ӵ�����(���ڽ������ݺ����������߼�) 
        acceptor.setHandler(  new TimeServerHandler() );
        //���ö�ȡ���ݻ��浥λbyte  
        acceptor.getSessionConfig().setReadBufferSize( 2048 );
        //���ö೤ʱ����������ʼ����
        acceptor.getSessionConfig().setIdleTime( IdleStatus.BOTH_IDLE, 10 );
     
        try {
            //��ĳ���˿ڣ���Ϊ�������  
            acceptor.bind( new InetSocketAddress(PORT) );
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}