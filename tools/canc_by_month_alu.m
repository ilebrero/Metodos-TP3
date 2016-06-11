% cerrar ventanas de matlab abiertas 
close all;

% orig_data tiene todos los datos (vectorizados) a mostrar.
% En el ejemplo de las cancelaciones, orig_data tiene las
% cancelaciones de cada mes.
% Grafica azul (default) con circulos en los datos.

plot(orig_data,'o-')


% Grafica lineas verticales en cada Enero, para separar los años. 
yval = get(gca,'ylim');
% m tiene la cantidad de años.
m = ;
hold on;
for idx = 1 : m
    plot([12*(idx-1)+1 12*(idx-1)+1], yval, 'k');
end

% Add years as x-values.
years = ...;
set(gca,'XTick',12*(0:m-1) + 6.5*ones(1,m));
set(gca,'XTickLabel',years);

% Aca iria el codigo de la regresion.

% p tiene los coeficientes de la regresion.
% xs el rango (y puntos intermedios) para graficar la regresion.
% ys la evaluacion de xs en p.
% grafica una linea roja.
p = ....;
xs = ...;
plot(xs,ys,'-r');


% Calculamos la estimacion.
% xs tiene los puntos a predecir.
% ys la evaluacion de p en xs.
% Grafica con cruces rojas.
x_pred = ....;
y_pred = ....;
plot(x_pred,y_pred,'xr');
