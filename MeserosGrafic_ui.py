<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1583</width>
    <height>842</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(10, 101, 112);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true">background-color: rgb(10, 101, 112);</string>
   </property>
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1581</width>
      <height>841</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(10, 101, 112);</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2" stretch="1,9">
     <property name="spacing">
      <number>0</number>
     </property>
     <property name="leftMargin">
      <number>0</number>
     </property>
     <property name="topMargin">
      <number>0</number>
     </property>
     <property name="rightMargin">
      <number>0</number>
     </property>
     <property name="bottomMargin">
      <number>0</number>
     </property>
     <item>
      <widget class="QFrame" name="frame_superior">
       <property name="minimumSize">
        <size>
         <width>0</width>
         <height>42</height>
        </size>
       </property>
       <property name="styleSheet">
        <string notr="true">QFrame{
background-color: rgb(255,255,255);
}

QPushButton{
background-color: #000000ff;
border-radius: 20px;
}

QPushButton{
background-color: rgb(101, 101, 101);
border-radius: 20px;
}

QPushButton:hover{
background-color: rgb(155,155,155);
border-radius: 20px;
color:  rgb(230,230,230);
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
}

</string>
       </property>
       <property name="frameShape">
        <enum>QFrame::StyledPanel</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Raised</enum>
       </property>
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="QPushButton" name="Boton_menu">
          <property name="minimumSize">
           <size>
            <width>400</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../Imagenes/menu (1).png</normaloff>../Imagenes/menu (1).png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>30</width>
            <height>30</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <spacer name="horizontalSpace_FrameSup">
          <property name="orientation">
           <enum>Qt::Horizontal</enum>
          </property>
          <property name="sizeHint" stdset="0">
           <size>
            <width>943</width>
            <height>20</height>
           </size>
          </property>
         </spacer>
        </item>
        <item>
         <widget class="QDateTimeEdit" name="Reloj">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 255, 255);</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="Boton_minimizar">
          <property name="minimumSize">
           <size>
            <width>40</width>
            <height>40</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../Imagenes/minimizar-signo.png</normaloff>../Imagenes/minimizar-signo.png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>30</width>
            <height>30</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="Boton_restaurar">
          <property name="minimumSize">
           <size>
            <width>40</width>
            <height>40</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../Imagenes/minimizar.png</normaloff>../Imagenes/minimizar.png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>30</width>
            <height>30</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="Boton_maximizar">
          <property name="minimumSize">
           <size>
            <width>40</width>
            <height>40</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../Imagenes/maximizar.png</normaloff>../Imagenes/maximizar.png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>30</width>
            <height>30</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="Boton_cerrar">
          <property name="minimumSize">
           <size>
            <width>40</width>
            <height>40</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>../Imagenes/cerrar.png</normaloff>../Imagenes/cerrar.png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>30</width>
            <height>30</height>
           </size>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QFrame" name="frame_inferior">
       <property name="styleSheet">
        <string notr="true"/>
       </property>
       <property name="frameShape">
        <enum>QFrame::StyledPanel</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Raised</enum>
       </property>
       <layout class="QHBoxLayout" name="horizontalLayout_2">
        <item>
         <widget class="QFrame" name="frame_control">
          <property name="minimumSize">
           <size>
            <width>400</width>
            <height>0</height>
           </size>
          </property>
          <property name="maximumSize">
           <size>
            <width>0</width>
            <height>16777215</height>
           </size>
          </property>
          <property name="styleSheet">
           <string notr="true">QFrame{
	background-color: rgb(255, 255, 255);
}

QPushButton{
	background-color: rgb(101, 101, 101);
	border-radius: 20px;
	color: rgb(230,230,230);
	font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
}


QPushButton:hover{
background-color: rgb(155,155,155);
border-radius: 20px;
color:  rgb(230,230,230);
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
}

</string>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
          <layout class="QVBoxLayout" name="verticalLayout_3">
           <item>
            <widget class="QPushButton" name="Boton_Atras">
             <property name="minimumSize">
              <size>
               <width>40</width>
               <height>70</height>
              </size>
             </property>
             <property name="styleSheet">
              <string notr="true">
QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(0, 170, 127);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
             </property>
             <property name="text">
              <string>ATRAS</string>
             </property>
            </widget>
           </item>
           <item>
            <widget class="QTableView" name="tabla__Pedido"/>
           </item>
           <item>
            <widget class="QPushButton" name="Boton_comfirmarPedido">
             <property name="minimumSize">
              <size>
               <width>0</width>
               <height>120</height>
              </size>
             </property>
             <property name="styleSheet">
              <string notr="true">
QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(0, 170, 127);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
             </property>
             <property name="text">
              <string>COMFIRMAR PEDIDO</string>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
        <item>
         <widget class="QFrame" name="frame_contenido">
          <property name="styleSheet">
           <string notr="true">QFrame{
background-color: rgb(101, 101, 101);
}

QLabel{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
background-color: #000000ff;
color:rgb(255,255,255);
border:0px solid#14C8DC;
}

QLineEdit{
border:0px;
color: rgb(10,10,10);
border-bottom:2px solid rgb(255,255,255);
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
}

QPushButton{
background-color: rgb(201, 201, 201);
border-radius: 15px;
color:  rgb(10,10,10);
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;

}
QPushButton:hover{
background-color: rgb(155,155,155);
border-radius: 15px;
color:  rgb(230,230,230);
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
}

QTableWidget{
background-color: rgb(255,255,255);
color:  rgb(230,230,230);
grindline-color: rgb(255,255,255);
font-size: 12pt;
color: #000000;
}

QHeaderView::section{
background-color: rgb(255,255,255);
border:1px solid rgb(10,10,10);
font-size: 12pt;
}

QTableWindget QTableCornerButtom::section{
background-color: rgb(205,205,205);
color:  rgb(255,255,255);
}
</string>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
          <layout class="QVBoxLayout" name="verticalLayout_4" stretch="0">
           <property name="spacing">
            <number>1</number>
           </property>
           <property name="leftMargin">
            <number>1</number>
           </property>
           <property name="topMargin">
            <number>1</number>
           </property>
           <property name="rightMargin">
            <number>1</number>
           </property>
           <property name="bottomMargin">
            <number>1</number>
           </property>
           <item>
            <widget class="QStackedWidget" name="stacked_Menu">
             <property name="currentIndex">
              <number>0</number>
             </property>
             <widget class="QWidget" name="pagina_usuarios">
              <widget class="QStackedWidget" name="stacked_controlPaginas">
               <property name="geometry">
                <rect>
                 <x>10</x>
                 <y>150</y>
                 <width>1131</width>
                 <height>571</height>
                </rect>
               </property>
               <property name="currentIndex">
                <number>3</number>
               </property>
               <widget class="QWidget" name="Pagina_Comida">
                <widget class="QWidget" name="layoutWidget_2">
                 <property name="geometry">
                  <rect>
                   <x>10</x>
                   <y>20</y>
                   <width>731</width>
                   <height>531</height>
                  </rect>
                 </property>
                 <layout class="QGridLayout" name="gridLayout_3">
                  <property name="sizeConstraint">
                   <enum>QLayout::SetMinAndMaxSize</enum>
                  </property>
                  <item row="0" column="3">
                   <widget class="QPushButton" name="Producto_3">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                    </property>
                    <property name="text">
                     <string>Producto 3</string>
                    </property>
                   </widget>
                  </item>
                  <item row="0" column="1">
                   <widget class="QPushButton" name="Mesa2_4">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                    </property>
                    <property name="text">
                     <string>Producto 1</string>
                    </property>
                   </widget>
                  </item>
                  <item row="0" column="2">
                   <widget class="QPushButton" name="Producto_2">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                    </property>
                    <property name="text">
                     <string>Producto 2</string>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </widget>
                <widget class="QWidget" name="layoutWidget_3">
                 <property name="geometry">
                  <rect>
                   <x>780</x>
                   <y>10</y>
                   <width>311</width>
                   <height>171</height>
                  </rect>
                 </property>
                 <layout class="QGridLayout" name="gridLayout_4">
                  <property name="sizeConstraint">
                   <enum>QLayout::SetMinAndMaxSize</enum>
                  </property>
                  <item row="1" column="1">
                   <widget class="QPushButton" name="Boton_ImprimirFactura">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <property name="layoutDirection">
                     <enum>Qt::RightToLeft</enum>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                    </property>
                    <property name="text">
                     <string>Imprimir</string>
                    </property>
                    <property name="icon">
                     <iconset>
                      <normaloff>../Imagenes/dinero.png</normaloff>../Imagenes/dinero.png</iconset>
                    </property>
                    <property name="iconSize">
                     <size>
                      <width>40</width>
                      <height>40</height>
                     </size>
                    </property>
                   </widget>
                  </item>
                  <item row="1" column="2">
                   <widget class="QPushButton" name="Boton_NotaDelProducto">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                    </property>
                    <property name="text">
                     <string>Nota</string>
                    </property>
                    <property name="icon">
                     <iconset>
                      <normaloff>../Imagenes/notas.png</normaloff>../Imagenes/notas.png</iconset>
                    </property>
                    <property name="iconSize">
                     <size>
                      <width>40</width>
                      <height>40</height>
                     </size>
                    </property>
                   </widget>
                  </item>
                  <item row="0" column="1">
                   <widget class="QPushButton" name="Boton_DescartarPedido">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <property name="layoutDirection">
                     <enum>Qt::RightToLeft</enum>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                    </property>
                    <property name="text">
                     <string>Descartar</string>
                    </property>
                    <property name="icon">
                     <iconset>
                      <normaloff>../Imagenes/descarte.png</normaloff>../Imagenes/descarte.png</iconset>
                    </property>
                    <property name="iconSize">
                     <size>
                      <width>50</width>
                      <height>50</height>
                     </size>
                    </property>
                   </widget>
                  </item>
                  <item row="0" column="2">
                   <widget class="QPushButton" name="Boton_Total">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <property name="layoutDirection">
                     <enum>Qt::RightToLeft</enum>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                    </property>
                    <property name="text">
                     <string>Total</string>
                    </property>
                    <property name="icon">
                     <iconset>
                      <normaloff>../Imagenes/factura.png</normaloff>../Imagenes/factura.png</iconset>
                    </property>
                    <property name="iconSize">
                     <size>
                      <width>50</width>
                      <height>50</height>
                     </size>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </widget>
                <widget class="QPushButton" name="Boton_AgregarProducto">
                 <property name="geometry">
                  <rect>
                   <x>780</x>
                   <y>470</y>
                   <width>331</width>
                   <height>61</height>
                  </rect>
                 </property>
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Minimum">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Yu Gothic UI Semibold</family>
                   <pointsize>15</pointsize>
                   <italic>false</italic>
                   <strikeout>false</strikeout>
                   <stylestrategy>PreferDefault</stylestrategy>
                   <fontweight></fontweight>
                  </font>
                 </property>
                 <property name="whatsThis">
                  <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;justify&quot;&gt;libre&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
                 </property>
                 <property name="layoutDirection">
                  <enum>Qt::LeftToRight</enum>
                 </property>
                 <property name="styleSheet">
                  <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                 </property>
                 <property name="text">
                  <string>Agregar Producto</string>
                 </property>
                 <property name="icon">
                  <iconset>
                   <normaloff>../Users/holan/OneDrive/Escritorio/tabla.png</normaloff>../Users/holan/OneDrive/Escritorio/tabla.png</iconset>
                 </property>
                 <property name="iconSize">
                  <size>
                   <width>100</width>
                   <height>100</height>
                  </size>
                 </property>
                </widget>
                <widget class="QPushButton" name="Boton_Cantidad">
                 <property name="geometry">
                  <rect>
                   <x>850</x>
                   <y>310</y>
                   <width>178</width>
                   <height>141</height>
                  </rect>
                 </property>
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Minimum">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Yu Gothic UI Semibold</family>
                   <pointsize>15</pointsize>
                   <italic>false</italic>
                   <strikeout>false</strikeout>
                   <stylestrategy>PreferDefault</stylestrategy>
                   <fontweight></fontweight>
                  </font>
                 </property>
                 <property name="whatsThis">
                  <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;justify&quot;&gt;libre&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
                 </property>
                 <property name="layoutDirection">
                  <enum>Qt::LeftToRight</enum>
                 </property>
                 <property name="styleSheet">
                  <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                 </property>
                 <property name="text">
                  <string>Cantidad</string>
                 </property>
                 <property name="icon">
                  <iconset>
                   <normaloff>../Users/holan/OneDrive/Escritorio/tabla.png</normaloff>../Users/holan/OneDrive/Escritorio/tabla.png</iconset>
                 </property>
                 <property name="iconSize">
                  <size>
                   <width>100</width>
                   <height>100</height>
                  </size>
                 </property>
                </widget>
                <widget class="QLineEdit" name="Line_Notas">
                 <property name="geometry">
                  <rect>
                   <x>780</x>
                   <y>210</y>
                   <width>311</width>
                   <height>91</height>
                  </rect>
                 </property>
                </widget>
               </widget>
               <widget class="QWidget" name="Pagina_Restaurantes">
                <layout class="QVBoxLayout" name="verticalLayout_8">
                 <item>
                  <layout class="QHBoxLayout" name="Layout_AgregarUsuario">
                   <item>
                    <layout class="QVBoxLayout" name="verticalLayout_7">
                     <property name="spacing">
                      <number>30</number>
                     </property>
                    </layout>
                   </item>
                   <item>
                    <layout class="QVBoxLayout" name="verticalLayout_6">
                     <property name="spacing">
                      <number>30</number>
                     </property>
                     <item>
                      <layout class="QGridLayout" name="gridLayout_2">
                       <property name="sizeConstraint">
                        <enum>QLayout::SetMinAndMaxSize</enum>
                       </property>
                       <item row="1" column="6">
                        <widget class="QPushButton" name="Restaurante_3">
                         <property name="sizePolicy">
                          <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                           <horstretch>0</horstretch>
                           <verstretch>0</verstretch>
                          </sizepolicy>
                         </property>
                         <property name="minimumSize">
                          <size>
                           <width>300</width>
                           <height>200</height>
                          </size>
                         </property>
                         <property name="styleSheet">
                          <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                         </property>
                         <property name="text">
                          <string>Restaurante 3</string>
                         </property>
                        </widget>
                       </item>
                       <item row="1" column="0">
                        <spacer name="horizontalSpacer">
                         <property name="orientation">
                          <enum>Qt::Horizontal</enum>
                         </property>
                         <property name="sizeHint" stdset="0">
                          <size>
                           <width>40</width>
                           <height>20</height>
                          </size>
                         </property>
                        </spacer>
                       </item>
                       <item row="1" column="4">
                        <widget class="QPushButton" name="Restaurante_2">
                         <property name="sizePolicy">
                          <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                           <horstretch>0</horstretch>
                           <verstretch>0</verstretch>
                          </sizepolicy>
                         </property>
                         <property name="minimumSize">
                          <size>
                           <width>300</width>
                           <height>200</height>
                          </size>
                         </property>
                         <property name="styleSheet">
                          <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                         </property>
                         <property name="text">
                          <string>Restaurante 2</string>
                         </property>
                        </widget>
                       </item>
                       <item row="1" column="3">
                        <widget class="QPushButton" name="Restaurante_1">
                         <property name="sizePolicy">
                          <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                           <horstretch>0</horstretch>
                           <verstretch>0</verstretch>
                          </sizepolicy>
                         </property>
                         <property name="minimumSize">
                          <size>
                           <width>300</width>
                           <height>200</height>
                          </size>
                         </property>
                         <property name="styleSheet">
                          <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                         </property>
                         <property name="text">
                          <string>Restaurante 1</string>
                         </property>
                        </widget>
                       </item>
                       <item row="1" column="7">
                        <spacer name="horizontalSpacer_2">
                         <property name="orientation">
                          <enum>Qt::Horizontal</enum>
                         </property>
                         <property name="sizeHint" stdset="0">
                          <size>
                           <width>40</width>
                           <height>20</height>
                          </size>
                         </property>
                        </spacer>
                       </item>
                      </layout>
                     </item>
                    </layout>
                   </item>
                  </layout>
                 </item>
                </layout>
               </widget>
               <widget class="QWidget" name="Pagina_Mesas">
                <layout class="QVBoxLayout" name="verticalLayout_12">
                 <item>
                  <layout class="QHBoxLayout" name="horizontalLayout_10">
                   <item>
                    <layout class="QGridLayout" name="gridLayout">
                     <property name="sizeConstraint">
                      <enum>QLayout::SetMinAndMaxSize</enum>
                     </property>
                     <item row="3" column="4">
                      <widget class="QPushButton" name="Mesa12">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="0" column="2">
                      <widget class="QPushButton" name="Mesa2">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="2" column="4">
                      <widget class="QPushButton" name="Mesa8">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="2" column="3">
                      <widget class="QPushButton" name="Mesa7">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="3" column="0">
                      <widget class="QPushButton" name="Mesa9">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="0" column="0">
                      <widget class="QPushButton" name="Mesa1">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="Preferred" vsizetype="Minimum">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="font">
                        <font>
                         <family>Yu Gothic UI Semibold</family>
                         <pointsize>15</pointsize>
                         <italic>false</italic>
                         <strikeout>false</strikeout>
                         <stylestrategy>PreferDefault</stylestrategy>
                         <fontweight></fontweight>
                        </font>
                       </property>
                       <property name="whatsThis">
                        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;justify&quot;&gt;libre&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
                       </property>
                       <property name="layoutDirection">
                        <enum>Qt::LeftToRight</enum>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                       <property name="icon">
                        <iconset>
                         <normaloff>../Users/holan/OneDrive/Escritorio/tabla.png</normaloff>../Users/holan/OneDrive/Escritorio/tabla.png</iconset>
                       </property>
                       <property name="iconSize">
                        <size>
                         <width>100</width>
                         <height>100</height>
                        </size>
                       </property>
                      </widget>
                     </item>
                     <item row="3" column="2">
                      <widget class="QPushButton" name="Mesa10">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="2" column="0">
                      <widget class="QPushButton" name="Mesa5">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="0" column="4">
                      <widget class="QPushButton" name="Mesa4">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="3" column="3">
                      <widget class="QPushButton" name="Mesa11">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="0" column="3">
                      <widget class="QPushButton" name="Mesa3">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                     <item row="2" column="2">
                      <widget class="QPushButton" name="Mesa6">
                       <property name="sizePolicy">
                        <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
                         <horstretch>0</horstretch>
                         <verstretch>0</verstretch>
                        </sizepolicy>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton{
font: 75 15pt &quot;Yu Gothic UI Semibold&quot;;
	color: rgb(0,0,0);
	background-color: rgb(38, 0, 0);
border-radius: 30px;

}
QPushButton{
background-color: rgb(230,230,230);
	color:rgb(0,0,0)

}
QPushButton:hover{
color: rgb(61, 61, 61);
	background-color: rgb(179, 179, 179);

}</string>
                       </property>
                       <property name="text">
                        <string>LIBRE</string>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </item>
                  </layout>
                 </item>
                </layout>
               </widget>
               <widget class="QWidget" name="Pagina_SeleccionMesero">
                <layout class="QVBoxLayout" name="verticalLayout_11">
                 <item>
                  <layout class="QHBoxLayout" name="horizontalLayout_9"/>
                 </item>
                 <item>
                  <spacer name="verticalSpacer_4">
                   <property name="orientation">
                    <enum>Qt::Vertical</enum>
                   </property>
                   <property name="sizeHint" stdset="0">
                    <size>
                     <width>20</width>
                     <height>40</height>
                    </size>
                   </property>
                  </spacer>
                 </item>
                 <item>
                  <layout class="QHBoxLayout" name="horizontalLayout_8">
                   <item>
                    <layout class="QVBoxLayout" name="verticalLayout_10">
                     <item>
                      <widget class="QPushButton" name="Mesero_1">
                       <property name="minimumSize">
                        <size>
                         <width>100</width>
                         <height>50</height>
                        </size>
                       </property>
                       <property name="text">
                        <string>Mesero 1</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QPushButton" name="Mesero_2">
                       <property name="minimumSize">
                        <size>
                         <width>100</width>
                         <height>50</height>
                        </size>
                       </property>
                       <property name="text">
                        <string>Mesero 2</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QPushButton" name="Mesero_3">
                       <property name="minimumSize">
                        <size>
                         <width>100</width>
                         <height>50</height>
                        </size>
                       </property>
                       <property name="text">
                        <string>Mesero 3</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QPushButton" name="Mesero_4">
                       <property name="minimumSize">
                        <size>
                         <width>100</width>
                         <height>50</height>
                        </size>
                       </property>
                       <property name="text">
                        <string>Mesero 4 </string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QPushButton" name="Mesero_5">
                       <property name="minimumSize">
                        <size>
                         <width>200</width>
                         <height>50</height>
                        </size>
                       </property>
                       <property name="text">
                        <string>Mesero 5</string>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </item>
                   <item>
                    <layout class="QVBoxLayout" name="verticalLayout_9">
                     <property name="spacing">
                      <number>30</number>
                     </property>
                     <item>
                      <widget class="QLineEdit" name="lineEdit_6">
                       <property name="minimumSize">
                        <size>
                         <width>0</width>
                         <height>40</height>
                        </size>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLineEdit" name="lineEdit_NombreUsuario_2">
                       <property name="minimumSize">
                        <size>
                         <width>0</width>
                         <height>40</height>
                        </size>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLineEdit" name="lineEdit_FuncionUsuario_2">
                       <property name="minimumSize">
                        <size>
                         <width>0</width>
                         <height>40</height>
                        </size>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLineEdit" name="lineEdit_ContrasenaUsuario_3">
                       <property name="minimumSize">
                        <size>
                         <width>0</width>
                         <height>40</height>
                        </size>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLineEdit" name="lineEdit_ContrasenaUsuario_2">
                       <property name="minimumSize">
                        <size>
                         <width>0</width>
                         <height>40</height>
                        </size>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </item>
                  </layout>
                 </item>
                 <item>
                  <spacer name="verticalSpacer_3">
                   <property name="orientation">
                    <enum>Qt::Vertical</enum>
                   </property>
                   <property name="sizeHint" stdset="0">
                    <size>
                     <width>20</width>
                     <height>40</height>
                    </size>
                   </property>
                  </spacer>
                 </item>
                 <item>
                  <layout class="QHBoxLayout" name="horizontalLayout_7">
                   <item>
                    <widget class="QLabel" name="label_14">
                     <property name="minimumSize">
                      <size>
                       <width>0</width>
                       <height>50</height>
                      </size>
                     </property>
                     <property name="text">
                      <string/>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QLabel" name="label_3">
                     <property name="text">
                      <string/>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <spacer name="horizontalSpacer_5">
                     <property name="orientation">
                      <enum>Qt::Horizontal</enum>
                     </property>
                     <property name="sizeHint" stdset="0">
                      <size>
                       <width>40</width>
                       <height>20</height>
                      </size>
                     </property>
                    </spacer>
                   </item>
                   <item>
                    <widget class="QPushButton" name="Boton_AceptarModificarUsuario">
                     <property name="minimumSize">
                      <size>
                       <width>300</width>
                       <height>100</height>
                      </size>
                     </property>
                     <property name="text">
                      <string>SELECCIONAR MESERO</string>
                     </property>
                    </widget>
                   </item>
                  </layout>
                 </item>
                </layout>
               </widget>
              </widget>
              <widget class="QWidget" name="layoutWidget">
               <property name="geometry">
                <rect>
                 <x>20</x>
                 <y>10</y>
                 <width>1121</width>
                 <height>131</height>
                </rect>
               </property>
               <layout class="QHBoxLayout" name="Layout_UsuariosCRUD">
                <property name="spacing">
                 <number>19</number>
                </property>
                <property name="leftMargin">
                 <number>9</number>
                </property>
                <property name="topMargin">
                 <number>9</number>
                </property>
                <property name="rightMargin">
                 <number>9</number>
                </property>
                <property name="bottomMargin">
                 <number>9</number>
                </property>
                <item>
                 <widget class="QPushButton" name="Boton_Mesas">
                  <property name="minimumSize">
                   <size>
                    <width>80</width>
                    <height>100</height>
                   </size>
                  </property>
                  <property name="text">
                   <string>MESAS</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="Boton_Restaurantes">
                  <property name="minimumSize">
                   <size>
                    <width>80</width>
                    <height>100</height>
                   </size>
                  </property>
                  <property name="text">
                   <string>RESTAURANTES</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="Boton_Comida">
                  <property name="minimumSize">
                   <size>
                    <width>80</width>
                    <height>100</height>
                   </size>
                  </property>
                  <property name="text">
                   <string>COMIDA</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="Boton_SeleccionMesero">
                  <property name="minimumSize">
                   <size>
                    <width>80</width>
                    <height>100</height>
                   </size>
                  </property>
                  <property name="maximumSize">
                   <size>
                    <width>300</width>
                    <height>16777215</height>
                   </size>
                  </property>
                  <property name="text">
                   <string>SELECCION MESERO</string>
                  </property>
                 </widget>
                </item>
               </layout>
              </widget>
             </widget>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
