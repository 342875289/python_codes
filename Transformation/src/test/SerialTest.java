package test;
import java.util.Enumeration;
import gnu.io.*;
public class SerialTest {
	@SuppressWarnings("rawtypes")
	static Enumeration portList; 
	static CommPortIdentifier portId;
	public static void main(String[] args) {
		try {
		      portList = CommPortIdentifier.getPortIdentifiers(); //�õ���ǰ�����ϵĶ˿�
		     System.out.println(portList.hasMoreElements());
		      while (portList.hasMoreElements()) {
		       portId = (CommPortIdentifier) portList.nextElement();
		       if (portId.getPortType() == CommPortIdentifier.PORT_SERIAL) {//�ж�����˿������Ǵ���
		        //if (portId.getName().equals("COM3")) { //�ж����COM3�˿��Ѿ�����������
		         System.out.println(portId.getName());
		        }
		       }
		      //}
		     } catch (Exception e) {
		    	 e.printStackTrace();
		     }  
	}

}
