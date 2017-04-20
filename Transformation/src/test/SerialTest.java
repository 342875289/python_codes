package test;
import java.util.Enumeration;
import gnu.io.*;
public class SerialTest {
	@SuppressWarnings("rawtypes")
	static Enumeration portList; 
	static CommPortIdentifier portId;
	public static void main(String[] args) {
		try {
		      portList = CommPortIdentifier.getPortIdentifiers(); //得到当前连接上的端口
		     System.out.println(portList.hasMoreElements());
		      while (portList.hasMoreElements()) {
		       portId = (CommPortIdentifier) portList.nextElement();
		       if (portId.getPortType() == CommPortIdentifier.PORT_SERIAL) {//判断如果端口类型是串口
		        //if (portId.getName().equals("COM3")) { //判断如果COM3端口已经启动就连接
		         System.out.println(portId.getName());
		        }
		       }
		      //}
		     } catch (Exception e) {
		    	 e.printStackTrace();
		     }  
	}

}
