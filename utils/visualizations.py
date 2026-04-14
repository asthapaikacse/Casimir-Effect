import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

class Visualizer:
    """
    Create interactive visualizations for the project
    """
    
    def __init__(self):
        self.color_scheme = {
            'primary': '#636EFA',
            'secondary': '#EF553B',
            'accent': '#00CC96',
            'critical_line': '#FF0000',
            'zero': '#FFD700',
            'vacuum': '#9B59B6',
            'casimir': '#3498DB'
        }
    
    def create_casimir_force_plot(self, distances, forces, plate_distance=None):
        """
        Interactive Casimir force vs distance plot
        """
        fig = go.Figure()
        
        # Main force curve
        fig.add_trace(go.Scatter(
            x=distances * 1e6,  # Convert to micrometers
            y=np.abs(forces) * 1e9,  # Convert to nN
            mode='lines',
            name='|F_Casimir|',
            line=dict(color=self.color_scheme['casimir'], width=3),
            fill='tozeroy',
            fillcolor='rgba(52, 152, 219, 0.3)',
            hovertemplate='Distance: %{x:.2f} μm<br>Force: %{y:.4f} nN<extra></extra>'
        ))
        
        # Mark experimental region
        fig.add_vrect(
            x0=0.1, x1=1.0,
            fillcolor="rgba(255, 215, 0, 0.2)",
            layer="below",
            line_width=0,
            annotation_text="Experimental Range",
            annotation_position="top left"
        )
        
        # Current plate position marker
        if plate_distance is not None:
            current_force = np.abs(np.interp(plate_distance, distances, np.abs(forces)))
            fig.add_trace(go.Scatter(
                x=[plate_distance * 1e6],
                y=[current_force * 1e9],
                mode='markers',
                marker=dict(size=20, color=self.color_scheme['zero'], 
                           symbol='star', line=dict(width=2, color='black')),
                name='Current Position',
                hovertemplate='Current Position<br>Distance: %{x:.3f} μm<br>Force: %{y:.4f} nN<extra></extra>'
            ))
        
        # FIXED: Use proper title syntax
        fig.update_layout(
            title_text='Casimir Force vs Plate Separation',
            title_font=dict(size=20, color='white'),
            title_x=0.5,
            xaxis=dict(
                title_text='Plate Separation (μm)',
                type='log',
                gridcolor='rgba(255,255,255,0.2)',
                title_font=dict(color='white'),
                tickfont=dict(color='white')
            ),
            yaxis=dict(
                title_text='|Force| (nN)',
                type='log',
                gridcolor='rgba(255,255,255,0.2)',
                title_font=dict(color='white'),
                tickfont=dict(color='white')
            ),
            paper_bgcolor='rgba(0,0,0,0.9)',
            plot_bgcolor='rgba(0,0,0,0.8)',
            font=dict(color='white'),
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                bgcolor='rgba(0,0,0,0.5)',
                bordercolor='white',
                borderwidth=1
            )
        )
        
        return fig
    
    def create_naive_sum_plot(self, n_values, partial_sums, zeta_value):
        """
        Show divergence of naive sum vs zeta regularization
        """
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Naive Sum (Divergent)', 'Zeta Regularization (Finite)'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Left plot: Divergent sum
        fig.add_trace(
            go.Scatter(
                x=n_values[:100],
                y=partial_sums[:100],
                mode='lines',
                name='Partial Sum',
                line=dict(color=self.color_scheme['secondary'], width=2),
                fill='tozeroy',
                fillcolor='rgba(239, 85, 59, 0.3)'
            ),
            row=1, col=1
        )
        
        fig.add_hline(
            y=0, line_dash="dash", line_color="white",
            annotation_text="Diverges to +∞", row=1, col=1
        )
        
        # Right plot: Zeta result
        fig.add_trace(
            go.Bar(
                x=['Zeta Regularization<br>ζ(-1) = -1/12'],
                y=[zeta_value],
                marker_color=self.color_scheme['accent'],
                text=[f'{zeta_value:.6f}'],
                textposition='outside',
                textfont=dict(size=16, color='white')
            ),
            row=1, col=2
        )
        
        # FIXED: Use proper title syntax
        fig.update_layout(
            title_text='The Infinite Sum Problem & Zeta Solution',
            title_font=dict(size=18, color='white'),
            title_x=0.5,
            paper_bgcolor='rgba(0,0,0,0.9)',
            plot_bgcolor='rgba(0,0,0,0.8)',
            font=dict(color='white'),
            showlegend=False,
            height=500
        )
        
        fig.update_xaxes(gridcolor='rgba(255,255,255,0.2)', row=1, col=1)
        fig.update_yaxes(title_text='Energy (arbitrary units)', 
                        gridcolor='rgba(255,255,255,0.2)', row=1, col=1)
        fig.update_yaxes(title_text='Regularized Value', 
                        gridcolor='rgba(255,255,255,0.2)', row=1, col=2)
        
        return fig
    
    def create_zeta_critical_line_plot(self, t_values, zeta_values, zeros=None):
        """
        Plot ζ(0.5 + it) on complex plane with zeros marked
        """
        fig = go.Figure()
        
        # Main curve
        fig.add_trace(go.Scatter(
            x=zeta_values.real,
            y=zeta_values.imag,
            mode='lines',
            name='ζ(0.5 + it)',
            line=dict(color=self.color_scheme['primary'], width=2),
            hovertemplate='Re: %{x:.4f}<br>Im: %{y:.4f}<extra></extra>'
        ))
        
        # Add direction arrows
        skip = len(t_values) // 20
        for i in range(0, len(t_values) - skip, skip):
            fig.add_annotation(
                x=zeta_values.real[i],
                y=zeta_values.imag[i],
                ax=zeta_values.real[i+skip//2],
                ay=zeta_values.imag[i+skip//2],
                xref='x', yref='y', axref='x', ayref='y',
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=1,
                arrowcolor='rgba(255,255,255,0.5)'
            )
        
        # Mark zeros
        if zeros is not None:
            for zero in zeros:
                if zero <= t_values[-1]:
                    # Find approximate zeta value at zero (should be near 0)
                    idx = np.argmin(np.abs(t_values - zero))
                    fig.add_trace(go.Scatter(
                        x=[zeta_values[idx].real],
                        y=[zeta_values[idx].imag],
                        mode='markers',
                        marker=dict(
                            size=15,
                            color=self.color_scheme['zero'],
                            symbol='x',
                            line=dict(width=2, color='black')
                        ),
                        name=f'Zero: t ≈ {zero:.2f}',
                        hovertemplate=f'Zero at t ≈ {zero:.4f}<extra></extra>'
                    ))
        
        # Mark origin
        fig.add_trace(go.Scatter(
            x=[0], y=[0],
            mode='markers',
            marker=dict(size=10, color='red', symbol='circle'),
            name='Origin (Zero Target)',
            hovertemplate='Origin<extra></extra>'
        ))
        
        # FIXED: Use proper title syntax
        fig.update_layout(
            title_text='Riemann Zeta Function on Critical Line: ζ(0.5 + it)',
            title_font=dict(size=18, color='white'),
            title_x=0.5,
            xaxis=dict(
                title_text='Re(ζ)',
                gridcolor='rgba(255,255,255,0.2)',
                zeroline=True, zerolinecolor='white', zerolinewidth=2,
                title_font=dict(color='white'),
                tickfont=dict(color='white')
            ),
            yaxis=dict(
                title_text='Im(ζ)',
                gridcolor='rgba(255,255,255,0.2)',
                zeroline=True, zerolinecolor='white', zerolinewidth=2,
                title_font=dict(color='white'),
                tickfont=dict(color='white'),
                scaleanchor='x', scaleratio=1
            ),
            paper_bgcolor='rgba(0,0,0,0.9)',
            plot_bgcolor='rgba(0,0,0,0.8)',
            font=dict(color='white'),
            hovermode='closest',
            showlegend=True,
            legend=dict(
                bgcolor='rgba(0,0,0,0.5)',
                bordercolor='white',
                borderwidth=1,
                yanchor='top', y=0.99, xanchor='left', x=0.01
            ),
            height=600
        )
        
        return fig
    
    def create_zeta_3d_surface(self, X, Y, magnitude, phase):
        """
        3D surface plot of |ζ(s)| over complex plane
        """
        # Clip magnitude for visualization
        mag_clipped = np.clip(magnitude, 0, 10)
        
        fig = go.Figure(data=[go.Surface(
            x=X, y=Y, z=mag_clipped,
            colorscale='Viridis',
            colorbar=dict(title='|ζ(s)|', tickfont=dict(color='white')),
            hovertemplate='Re(s): %{x:.2f}<br>Im(s): %{y:.2f}<br>|ζ|: %{z:.4f}<extra></extra>'
        )])
        
        # Mark critical line
        critical_x = np.full_like(Y[:, 0], 0.5)
        critical_z = np.zeros_like(Y[:, 0])
        
        fig.add_trace(go.Scatter3d(
            x=critical_x,
            y=Y[:, 0],
            z=critical_z,
            mode='lines',
            line=dict(color='red', width=5),
            name='Critical Line Re(s)=0.5'
        ))
        
        # FIXED: Use proper title syntax
        fig.update_layout(
            title_text='|ζ(s)| over Complex Plane',
            title_font=dict(size=18, color='white'),
            title_x=0.5,
            scene=dict(
                xaxis=dict(title_text='Re(s)', gridcolor='gray', title_font=dict(color='white')),
                yaxis=dict(title_text='Im(s)', gridcolor='gray', title_font=dict(color='white')),
                zaxis=dict(title_text='|ζ(s)|', gridcolor='gray', title_font=dict(color='white')),
                bgcolor='rgba(0,0,0,0.8)'
            ),
            paper_bgcolor='rgba(0,0,0,0.9)',
            font=dict(color='white'),
            height=700
        )
        
        return fig
    
    def create_domain_coloring(self, X, Y, Z, magnitude, phase):
        """
        Domain coloring visualization of zeta function
        """
        # Create HSV color mapping
        from matplotlib.colors import hsv_to_rgb
        
        hue = (phase + np.pi) / (2 * np.pi)  # Normalize to [0, 1]
        saturation = np.ones_like(hue)
        value = np.clip(1 - np.exp(-magnitude/5), 0, 1)  # Soft clipping
        
        hsv = np.stack([hue, saturation, value], axis=-1)
        rgb = hsv_to_rgb(hsv)
        
        fig = go.Figure(data=go.Image(
            z=(rgb * 255).astype(np.uint8),
            x0=X.min(), y0=Y.min(),
            dx=(X.max() - X.min()) / X.shape[1],
            dy=(Y.max() - Y.min()) / Y.shape[0],
            hovertemplate='Re: %{x:.2f}<br>Im: %{y:.2f}<extra></extra>'
        ))
        
        # Add critical line
        fig.add_vline(x=0.5, line_width=3, line_color='red', 
                     line_dash='dash', opacity=0.8)
        
        # Add annotation for critical line
        fig.add_annotation(
            x=0.5, y=Y.max(),
            text='Critical Line',
            showarrow=False,
            font=dict(color='red', size=12),
            bgcolor='black',
            opacity=0.8
        )
        
        # FIXED: Use proper title syntax
        fig.update_layout(
            title_text='Domain Coloring: ζ(s) (Hue=Phase, Brightness=|ζ|)',
            title_font=dict(size=18, color='white'),
            title_x=0.5,
            xaxis=dict(
                title_text='Re(s)',
                gridcolor='rgba(255,255,255,0.2)',
                title_font=dict(color='white'),
                tickfont=dict(color='white')
            ),
            yaxis=dict(
                title_text='Im(s)',
                gridcolor='rgba(255,255,255,0.2)',
                title_font=dict(color='white'),
                tickfont=dict(color='white'),
                scaleanchor='x'
            ),
            paper_bgcolor='rgba(0,0,0,0.9)',
            plot_bgcolor='rgba(0,0,0,0.8)',
            font=dict(color='white'),
            height=600
        )
        
        return fig
    
    def create_real_imaginary_plot(self, t_values, zeta_values, zeros=None):
        """
        Separate plots for real and imaginary parts along critical line
        """
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            subplot_titles=('Re(ζ(0.5 + it))', 'Im(ζ(0.5 + it))'),
            vertical_spacing=0.1
        )
        
        # Real part
        fig.add_trace(
            go.Scatter(
                x=t_values,
                y=zeta_values.real,
                mode='lines',
                name='Re(ζ)',
                line=dict(color=self.color_scheme['primary'], width=2),
                fill='tozeroy',
                fillcolor='rgba(99, 110, 250, 0.2)'
            ),
            row=1, col=1
        )
        
        # Imaginary part
        fig.add_trace(
            go.Scatter(
                x=t_values,
                y=zeta_values.imag,
                mode='lines',
                name='Im(ζ)',
                line=dict(color=self.color_scheme['secondary'], width=2),
                fill='tozeroy',
                fillcolor='rgba(239, 85, 59, 0.2)'
            ),
            row=2, col=1
        )
        
        # Mark zeros - FIXED: Use loop instead of row='all'
        if zeros is not None:
            for zero in zeros:
                if zero <= t_values[-1]:
                    # Add vline for row 1
                    fig.add_vline(
                        x=zero, line_dash="dash", line_color=self.color_scheme['zero'],
                        opacity=0.7, row=1, col=1
                    )
                    # Add vline for row 2
                    fig.add_vline(
                        x=zero, line_dash="dash", line_color=self.color_scheme['zero'],
                        opacity=0.7, row=2, col=1
                    )
        
        # Zero lines
        fig.add_hline(y=0, line_dash="dash", line_color="white", 
                     opacity=0.5, row=1, col=1)
        fig.add_hline(y=0, line_dash="dash", line_color="white", 
                     opacity=0.5, row=2, col=1)
        
        # FIXED: Use proper title syntax
        fig.update_layout(
            title_text='Real and Imaginary Parts along Critical Line',
            title_font=dict(size=18, color='white'),
            title_x=0.5,
            paper_bgcolor='rgba(0,0,0,0.9)',
            plot_bgcolor='rgba(0,0,0,0.8)',
            font=dict(color='white'),
            showlegend=False,
            height=700
        )
        
        fig.update_xaxes(title_text='t (Im(s))', gridcolor='rgba(255,255,255,0.2)', row=2, col=1)
        fig.update_yaxes(gridcolor='rgba(255,255,255,0.2)', row=1, col=1)
        fig.update_yaxes(gridcolor='rgba(255,255,255,0.2)', row=2, col=1)
        
        return fig
    
    def create_prime_connection_plot(self, x_values, pi_x, li_x, primes):
        """
        Show connection between zeta zeros and prime distribution
        """
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Prime Counting Function', 'Error: Li(x) - π(x)'),
            vertical_spacing=0.15
        )
        
        # Top: Prime counting
        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=pi_x,
                mode='lines',
                name='π(x) - Exact',
                line=dict(color=self.color_scheme['accent'], width=2)
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=li_x,
                mode='lines',
                name='Li(x) - Zeta-based Approx',
                line=dict(color=self.color_scheme['primary'], width=2, dash='dash')
            ),
            row=1, col=1
        )
        
        # Mark actual primes
        prime_y = [sum(1 for p in primes if p <= x) for x in primes]
        fig.add_trace(
            go.Scatter(
                x=primes,
                y=prime_y,
                mode='markers',
                marker=dict(size=6, color=self.color_scheme['zero'], 
                           symbol='circle', opacity=0.7),
                name='Primes',
                hovertemplate='Prime: %{x}<extra></extra>'
            ),
            row=1, col=1
        )
        
        # Bottom: Error
        error = li_x - pi_x
        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=error,
                mode='lines',
                name='Error',
                line=dict(color=self.color_scheme['secondary'], width=2),
                fill='tozeroy',
                fillcolor='rgba(239, 85, 59, 0.2)'
            ),
            row=2, col=1
        )
        
        # FIXED: Use proper title syntax
        fig.update_layout(
            title_text='Zeta Function & Prime Number Connection',
            title_font=dict(size=18, color='white'),
            title_x=0.5,
            paper_bgcolor='rgba(0,0,0,0.9)',
            plot_bgcolor='rgba(0,0,0,0.8)',
            font=dict(color='white'),
            showlegend=True,
            legend=dict(
                bgcolor='rgba(0,0,0,0.5)',
                bordercolor='white',
                borderwidth=1
            ),
            height=700
        )
        
        fig.update_xaxes(gridcolor='rgba(255,255,255,0.2)', row=1, col=1)
        fig.update_xaxes(title_text='x', gridcolor='rgba(255,255,255,0.2)', row=2, col=1)
        fig.update_yaxes(title_text='Count', gridcolor='rgba(255,255,255,0.2)', row=1, col=1)
        fig.update_yaxes(title_text='Error', gridcolor='rgba(255,255,255,0.2)', row=2, col=1)
        
        return fig
    
    def create_conceptual_diagram(self):
        """
        Create a conceptual flow diagram
        """
        fig = go.Figure()
        
        # Define nodes
        nodes = [
            {'x': 0, 'y': 4, 'text': 'Quantum Vacuum<br>❌ Not Empty', 'color': '#9B59B6'},
            {'x': 0, 'y': 3, 'text': 'Casimir Effect<br>✓ Experimental Proof', 'color': '#3498DB'},
            {'x': 0, 'y': 2, 'text': 'Infinite Energy Sum<br>⚠ Divergence Problem', 'color': '#E74C3C'},
            {'x': 0, 'y': 1, 'text': 'Zeta Regularization<br>💡 ζ(-1) = -1/12', 'color': '#F39C12'},
            {'x': 0, 'y': 0, 'text': 'Riemann Hypothesis<br>🔥 Millennium Problem', 'color': '#E91E63'}
        ]
        
        # Add nodes
        for node in nodes:
            fig.add_trace(go.Scatter(
                x=[node['x']],
                y=[node['y']],
                mode='markers+text',
                marker=dict(size=60, color=node['color'], 
                           line=dict(width=3, color='white')),
                text=node['text'],
                textposition='middle center',
                textfont=dict(size=12, color='white', family='Arial Black'),
                hoverinfo='text',
                showlegend=False
            ))
        
        # Add connecting arrows
        for i in range(len(nodes) - 1):
            fig.add_annotation(
                x=nodes[i]['x'],
                y=nodes[i]['y'] - 0.3,
                ax=nodes[i+1]['x'],
                ay=nodes[i+1]['y'] + 0.3,
                xref='x', yref='y', axref='x', ayref='y',
                showarrow=True,
                arrowhead=2,
                arrowsize=1.5,
                arrowwidth=2,
                arrowcolor='white'
            )
        
        # Add side connections
        fig.add_annotation(
            x=0.5, y=1,
            text='Physics → Math',
            showarrow=False,
            font=dict(color='white', size=10),
            bgcolor='rgba(0,0,0,0.5)'
        )
        
        # FIXED: Use proper title syntax
        fig.update_layout(
            title_text='Project Concept Flow',
            title_font=dict(size=20, color='white'),
            title_x=0.5,
            xaxis=dict(
                range=[-1, 1],
                showgrid=False,
                showticklabels=False,
                zeroline=False
            ),
            yaxis=dict(
                range=[-0.5, 4.5],
                showgrid=False,
                showticklabels=False,
                zeroline=False
            ),
            paper_bgcolor='rgba(0,0,0,0.9)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=600,
            showlegend=False
        )
        
        return fig
